def square(num):
    return x**2

result = [f(x) for x in list(range(100000))]

from multiprocessing import Pool
pool = Pool(8)
result = pool.map(f,list(range(100000)))
pool.close()
