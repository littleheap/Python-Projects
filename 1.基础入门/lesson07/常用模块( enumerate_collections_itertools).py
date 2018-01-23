print("----------enumerate----------")
# 对一个列表或数组既要遍历索引又要遍历元素时
l = [1, 2, 3]
for i in range(len(l)):
    print(i, l[i])

print("--------------------")

# enumerate会将数组或列表组成一个索引序列。使我们再获取索引和索引内容的时候更加方便如下：
for index, text in enumerate(l):
    print(index, text)

print("----------collection----------")

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

print("--------------------")

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

print("--------------------")

from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])  # key1存在
print(dd['key2'])  # key2不存在，返回默认值

print("--------------------")

from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)  # dict的Key是无序的，{'a': 1, 'c': 3, 'b': 2}
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)  # OrderedDict的Key是有序的，OrderedDict([('a', 1), ('b', 2), ('c', 3)])

print("--------------------")

from collections import Counter

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)  # Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})

print("----------itertooles----------")

import itertools

for i in zip(itertools.count(1), ['a', 'b', 'c']):
    print(i)
