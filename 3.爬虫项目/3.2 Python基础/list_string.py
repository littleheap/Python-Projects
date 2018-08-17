s = 'abcdefg'
try:
    str[0] = 'x'
except Exception as e:
    print(e)  # 'type' object does not support item assignment

# 修改字符串
li = list(s)
print(li)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']

li[0] = 'x'
s = ''.join(li)
print(s)  # xbcdefg

s = '-'.join(li)
print(s)  # x-b-c-d-e-f-g

# 切割
s = 'abc,def,ghi'
p1, p2, p3 = s.split(',')
print(p1, p2, p3)  # abc def ghi

# 下标访问和切片
s = 'abcdefg'
print(s[0], s[-1])  # a g
print(s[2:5])  # cde
