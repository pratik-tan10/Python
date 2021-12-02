
from multiprocessing import Pool
import time
import plotly.express as px
import plotly
import pandas as pd
from joblib import Parallel, delayed

def f(x):
    time.sleep(2)
    return x**2


def runner(list_length):
    print(f"Size of List:{list_length}")
    t0 = time.time()
    result1 = Parallel(n_jobs=8)(delayed(f)(i) for i in range(list_length))
    t1 = time.time()
    print(f"With joblib we ran the function in {t1 - t0:0.4f} seconds")
    time_without_multiprocessing = t1-t0
    t0 = time.time()
    pool = Pool(8)
    result2 = pool.map(f,list(range(list_length)))
    pool.close()
    t1 = time.time()
    print(f"With multiprocessing we ran the function in {t1 - t0:0.4f} seconds")
    time_with_multiprocessing = t1-t0
    return time_without_multiprocessing, time_with_multiprocessing

if __name__ ==  '__main__':
    times_taken = []
    for i in range(1,16):
        list_length = i
        time_without_multiprocessing, time_with_multiprocessing = runner(list_length)
        times_taken.append([list_length, 'No Mutiproc', time_without_multiprocessing])
        times_taken.append([list_length, 'Multiproc', time_with_multiprocessing])

    timedf = pd.DataFrame(times_taken,columns = ['list_length', 'type','time_taken'])
    fig =  px.line(timedf,x = 'list_length',y='time_taken',color='type')
    plotly.offline.plot(fig, filename='comparison_bw_multiproc.html')
    
#Multiprocessing using multiple params function
import random
def model_runner(n_estimators, max_depth):
    # Some code that runs and fits our model here using the   
    # hyperparams in the argument.
    # Proxy for this code with sleep.
    time.sleep(random.choice([1,2,3])
    # Return some model evaluation score
    return random.choice([1,2,3])

#using pool.map and magic
def multi_run_wrapper(args):
   return model_runner(*args)
pool = Pool(4)
hyperparams = [[100,4],[150,5],[200,6],[300,4]]
results = pool.map(multi_run_wrapper,hyperparams)

#Using pool.starmap
pool = Pool(4)
hyperparams = [[100,4],[150,5],[200,6],[300,4]]
results = pool.starmap(model_runner,hyperparams)
pool.close()


pool.close()

#Using joblib and single param function
from joblib import Parallel, delayed
import time
def f(x):
    time.sleep(2)
    return x**2
results = Parallel(n_jobs=8)(delayed(f)(i) for i in range(10))

#Using joblib with multiple params function
from joblib import Parallel, delayed
import time
def f(x,y):
    time.sleep(2)
    return x**2 + y**2
params = [[x,x] for x in range(10)]
results = Parallel(n_jobs=8)(delayed(f)(x,y) for x,y in params)
