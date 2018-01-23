'''
    顺序执行单线程与同时执行两个并发线程
    join()会阻塞，知道当前线程执行完毕
'''
from threading import Thread


def my_counter():
    i = 0
    for _ in range(100000000):
        i = i + 1
    return True


def main():
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter)
        t.start()
        t.join()
    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))


# main()


def my_counter():
    i = 0
    for _ in range(100000000):
        i = i + 1
    return True


def main():
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter)
        t.start()
        thread_array[tid] = t
    for i in range(2):
        thread_array[i].join()
    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))


# main()

'''
    多进程multiprocessing
'''


def f(n):
    time.sleep(1)
    print(n * n)


def main():
    for i in range(10):
        p = Process(target=f, args=[i, ])
        p.start()


# if __name__ == '__main__':
#     main()

'''
    进程间通信Queue
'''
from multiprocessing import Queue


def write(q):
    for i in ['A', 'B', 'C', 'D', 'E']:
        print('Put %s to queue' % i)
        q.put(i)
        time.sleep(0.5)


def read(q):
    while True:
        v = q.get(True)
        print('get %s from queue' % v)
        if (v == 'E'): break;


def main():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pr.join()
    pr.terminate()


# if __name__ == '__main__':
# main()

'''
    进程池Pool
'''
from multiprocessing import Pool


def f(x):
    print(x * x)
    time.sleep(2)
    return x * x


def main():
    # 定义启动的进程数量
    pool = Pool(processes=5)
    res_list = []

    for i in range(10):
        '''
            以异步并行的方式启动进程
            如果要同步等待的方式，可以在每次启动进程之后调用res.get()方法，也可以使用Pool.apply
        '''
        res = pool.apply_async(f, [i, ])
        print('-------:', i)
        res_list.append(res)
    pool.close()
    pool.join()
    for r in res_list:
        print("result", (r.get(timeout=5)))


# if __name__ == '__main__':
#     main()

'''
    多进程与多线程对比：
    1.进程不共享内存资源
    2.线程可以共享内存资源
'''
from multiprocessing import Process
import threading
import time

# 进程锁
lock = threading.Lock()


def run(info_list, n):
    lock.acquire()
    info_list.append(n)
    lock.release()
    print('%s\n' % info_list)


def main():
    info = []
    for i in range(10):
        # target为子进程执行的函数，args为需要给函数传递的参数
        p = Process(target=run, args=[info, i])
        p.start()
        p.join()
    # 这里是为了输出整齐让主进程的执行等一下子进程
    time.sleep(1)
    print('------------threading--------------')
    for i in range(10):
        p = threading.Thread(target=run, args=[info, i])
        p.start()
        p.join()


# if __name__ == '__main__':
#     main()

