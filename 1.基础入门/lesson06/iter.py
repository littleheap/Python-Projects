# 实现for一个类，要实现iter和next两个方法
class Fib100:
    def __init__(self):
        self._1, self._2 = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self._1, self._2 = self._2, self._1 + self._2
        if self._1 > 100:
            raise StopIteration()
        return self._1


for i in Fib100():
    print(i)
