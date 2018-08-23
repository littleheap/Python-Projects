# FIFO: 先进先出
# LIFO: 后进先出
# Priority Queue

import queue
import threading

q = queue.Queue()
for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())

q = queue.LifoQueue()
for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())


class Task:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __lt__(self, other):  # Python 2.7, implement __cmp__
        return self.priority < other.priority


q = queue.PriorityQueue()
q.put(Task(1, 'Important task'))
q.put(Task(10, 'Normal task'))
q.put(Task(100, 'Lazy task'))


def job(q):
    while True:
        task = q.get()
        print('Task: %s\n' % task.description)
        q.task_done()


threads = [threading.Thread(target=job, args=(q,)), threading.Thread(target=job, args=(q,))]
for t in threads:
    t.setDaemon(True)
    t.start()
q.join()

'''
    0
    1
    2
    3
    4
    4
    3
    2
    1
    0
    Task: Important task
    
    Task: Normal task
    
    Task: Lazy task
'''
