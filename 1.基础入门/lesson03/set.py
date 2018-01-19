s_a = set([1, 2, 2, 3, 4, 5, 6])
s_b = set([4, 5, 6, 7, 8, 9])
print(s_a)
print(s_b)

# 判断元素是否存在
print(5 in s_a)
print(10 in s_b)

# 并集
print(s_a | s_b)
print(s_a.union(s_b))

# 交集
print(s_a & s_b)
print(s_a.intersection(s_b))

# 差集 A - (A & B)
print(s_a - s_b)
print(s_a.difference(s_b))

# 对称差 (A | B) - (A & B)
print(s_a ^ s_b)
print(s_a.symmetric_difference(s_b))

# 修改元素
s_a.add('x')
s_a.update([4, 5, 60, 70])
print(s_a)
s_a.remove(70)
print(s_a)
# s_a.remove(100)

print(len(s_a))
for i in s_a:
    print(i)
