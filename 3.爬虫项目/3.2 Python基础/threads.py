import threading


def thread_func(x):
    print('%d\n' % (x * 100))


threads = []
for i in range(5):
    threads.append(threading.Thread(target=thread_func, args=(100,)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

'''
    10000
    
    10000
    
    10000
    
    10000
    
    10000
'''
