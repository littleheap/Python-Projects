import time, threading


def loop():
    thread_name = threading.current_thread().name
    print('Thread %s is running...' % thread_name)
    n = 0
    while n < 5:
        n = n + 1
        print('Thread %s >>> %d' % (thread_name, n))
    print('Thread %s ends.' % thread_name)


thread_name = threading.current_thread().name
print('Thread %s is running...' % thread_name)
t = threading.Thread(target=loop, name='loopThread')
t.start()
t.join()
print('Thread %s ends.' % thread_name)

'''
Thread MainThread is running...
Thread loopThread is running...
Thread loopThread >>> 1
Thread loopThread >>> 2
Thread loopThread >>> 3
Thread loopThread >>> 4
Thread loopThread >>> 5
Thread loopThread ends.
Thread MainThread ends.
'''