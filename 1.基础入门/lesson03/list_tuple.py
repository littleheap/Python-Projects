# list中可以存放任何类型的数据
li = [1, 2, 3, '456', [1, 2, 3], {1: 'one', 2: 'two'}]
print(type(list))
print(type(li))

# 元素访问
print(li[0])
print(li[-1])  # li[len(li) - 1]
print(li[-2])  # li[len(li) - 2]

# 查找元素位置
print(li.index('456'))
print(li.index([1, 2, 3]))
# print(li.index(-1))

# 添加元素
l_a = [1, 2, 3]
l_a.append(4)
l_a.append(5)
l_b = [6, 7, 8]
l_a.extend(l_b)  # 试下用append是什么结果
print(l_a)

l_a = []
if not l_a:  # 用来判断是否为空
    print('Empty')  # not XX和is None不是一回事

if len(l_a) == 0:
    print('Empty')

for i in li:
    print(i)
for i in range(len(li)):
    print(li[i])

t = (1, 2, 3, '456')
print(type(t))
# tuple类型元组不能修改
# t[0] = 'a'
# 也不能append
# t.append('x')

# 删除元素
del (li[-1])  # del(list[index])
del (li[1])
del (li[-2])
print(li)
