# strip去除空格
s = ' abcd efg  '
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s)

# 字符串连接
print('abc_' + 'defg')
s = 'abcdefg'
s += '\nhijk'
print(str)

# 大写小
s = 'abc defg'
print(s.upper())
print(s.upper().lower())
print(s.capitalize())

# 位置和比较
s_1 = 'abcdefg'
s_2 = 'abdefgh'
print(s_1.index('bcd'))
try:
    print(s_1.index('bce'))
except ValueError:
    print('ValueError: substring not found')
print(s_1 == s_1)  # cmp函数被Python3移除了
print(s_1 > s_2)
print(s_2 > s_1)

# 分割和连接
s = 'abc,def,ghi'
print(s.split(','))
s = '123\n456\n789'
numbers = s.splitlines()
print(numbers)
print('-'.join(numbers))

# 常用判断
s = 'abcdefg'
print(s.startswith('abc'))
print(s.endswith('efg'))
print('abcd1234'.isalnum())
print('\tabcd1234'.isalnum())
print('abcd'.isalpha())
print('12345'.isdigit())
print('  '.isspace())
print('acb125'.islower())
print('A1B2C'.isupper())
print('Hello world!'.istitle())

# 数字到字符串
print(str(5))
print(str(5.))
print(str(-5.23))
print(int('1234'))
print(float('-23.456'))

# 格式化字符串
print('Hello %s!' % 'world')
print('%d-%.2f-%s' % (4, -2.3, 'hello'))
