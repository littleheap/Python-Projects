import time
import threadpool


def long_op(n):
    print('%d\n' % n)
    time.sleep(2)


pool = threadpool.ThreadPool(2)
tasks = threadpool.makeRequests(long_op, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(len(tasks))
[pool.putRequest(task) for task in tasks]
pool.wait()

'''
    10
    1
    2
    
    
    3
    4
    
    
    5
    
    6
    
    7
    
    8
    
    9
    
    10
'''