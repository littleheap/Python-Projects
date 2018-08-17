li = [1, 2, 3, 4, 5]

# 遍历
for i in li:
    print(i)
'''
    1
    2
    3
    4
    5
'''

# range(x) => [0, x - 1]
# range(x, y) => [x, y - 1]
# range(x, y, z) => [x, x + z,..., < y]
for i in range(len(li)):
    print(li[i])
'''
    1
    2
    3
    4
    5
'''

for i in range(1, 10, 2):
    print(i)
'''
    1
    3
    5
    7
    9
'''

# 负数索引
print(li[-1])  # 5
print(li[-2])  # 4

# 负数step的range => [x, x - z, ..., > z]
for i in range(3, -1, -1):
    print(i)
'''
    3
    2
    1
    0
'''

# 添加元素
li = []
li.append(1)
li.append(2)
li.append('abc')
li.append(['d', 'e', 'f'])
print(li)  # [1, 2, 'abc', ['d', 'e', 'f']]

# 按元素添加数组
li = [1, 2]
li_2 = [3, 4, 5]
# 我们想要[1, 2, 3, 4, 5]
# li.append(li_2) => [1, 2, [3, 4, 5]]
li.extend(li_2)
print(li)  # [1, 2, 3, 4, 5]

# 删除元素
li.pop()  # [1, 2, 3, 4]
print(li)
li.pop(2)  # [1, 2, 4]
print(li)

li = [5, 8, 7, 4, 2, 3]
li.sort()
print(li)  # [2, 3, 4, 5, 7, 8]

# lambda帮助排序
li = [[5, 2], [3, 8], [2, 11], [7, 6]]
li.sort(key=lambda x: x[0])  # 参数名字


# 与lamda等价写法
def item_key(x):
    return x[0]


li.sort(key=item_key)
print(li)  # [[2, 11], [3, 8], [5, 2], [7, 6]]
