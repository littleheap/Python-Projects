import threading

def thread_func(x):
    # 自己加sleep和其它复杂操作看效果
    print('%d\n' % (x * 100))

threads = []
for i in range(5):
    threads.append(threading.Thread(target = thread_func, args = (100, )))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
