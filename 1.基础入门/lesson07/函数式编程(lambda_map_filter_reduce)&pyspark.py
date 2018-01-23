'''
    函数式编程
'''


def inc(x):
    def incx(y):
        return x + y

    return incx


inc2 = inc(2)
inc5 = inc(5)

# print(inc2(5))  # 输出 7
# print(inc5(5))  # 输出 10

g = lambda x: x * 2
# print(g(3))
# print(lambda x: x * 2)(4)

# for n in ["qi", "yue", "July"]:
#     print(len(n))

'''
    map
'''
name_len = list(map(len, ["qi", "yue", "July"]))


# print(name_len)

def toUpper(item):
    return item.upper()


upper_name = map(toUpper, ["qi", "yue", "July"])
# print(list(upper_name))

items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i ** 2)
# print(squared)

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))
# print(squared)

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))

# print(less_than_zero)

'''
    reduce
'''
from functools import reduce


def add(x, y): return x + y


# print(reduce(add, range(1, 5)))
# print(reduce(add, range(1, 5), 10))

'''
    例：计算数组中正数的平均数
'''
# 正常写法：
num = [2, -5, 9, 7, -2, 5, 3, 1, 0, -3, 8]
positive_num_cnt = 0
positive_num_sum = 0
for i in range(len(num)):
    if num[i] > 0:
        positive_num_cnt += 1
        positive_num_sum += num[i]

if positive_num_cnt > 0:
    average = positive_num_sum / positive_num_cnt

# print(average)

# 函数式写法：
num = [2, -5, 9, 7, -2, 5, 3, 1, 0, -3, 8]
positive_num = list(filter(lambda x: x > 0, num))
# print(positive_num)
average = reduce(lambda x, y: x + y, positive_num) / len(positive_num)
# print(average)

'''
    pyspark
'''
from operator import add
from pyspark import SparkContext

sc = SparkContext()

lines = sc.textFile("stormofswords.csv")
counts = lines.flatMap(lambda x: x.split(',')) \
    .map(lambda x: (x, 1)) \
    .reduceByKey(add)
output = counts.collect()
output = list(filter(lambda x: not x[0].isnumeric(), sorted(output, key=lambda x: x[1], reverse=True)))
for (word, count) in output[:10]:
    print("%s: %i" % (word, count))
sc.stop()
