from multiprocessing import Pool
import time
import plotly.express as px
import plotly
import pandas as pd

def f(x):
    return x**2

def runner(list_length):
    print(f"Size of List:{list_length}")
    t0 = time.time()
    result1 = [f(x) for x in list(range(list_length))]
    t1 = time.time()
    print(f"Without multiprocessing we ran the function in {t1 - t0:0.4f} seconds")
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
    for i in range(1,9):
        list_length = 10**i
        time_without_multiprocessing, time_with_multiprocessing = runner(list_length)
        times_taken.append([list_length, 'No Mutiproc', time_without_multiprocessing])
        times_taken.append([list_length, 'Multiproc', time_with_multiprocessing])

    timedf = pd.DataFrame(times_taken,columns = ['list_length', 'type','time_taken'])
    fig =  px.line(timedf,x = 'list_length',y='time_taken',color='type',log_x=True)
    plotly.offline.plot(fig, filename='comparison_bw_multiproc.html')
