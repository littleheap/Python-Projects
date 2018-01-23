import re

# match从开头搜索
m = re.match(r'dog', 'dog cat dog')
print(m.group())
print(re.match(r'cat', 'dog cat dog'))

# search不一定从开头搜索
s = re.search(r'cat', 'dog cat dog')
print(s.group())

# findall找寻所有匹配
print(re.findall(r'dog', 'dog cat dog'))

print("-------------------")

# group()分组，\w是字符，\S是数字
contactInfo = 'Doe, John: 555-1212'
m = re.search(r'(\w+), (\w+): (\S+)', contactInfo)
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.group(0))

print("-------------------")

# email example
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
    print(match.group())  # 'b@google',因为\w不能匹配到地址中的'-'和'.'

print("-------------------")

match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print(match.group())  # 'alice-b@google.com'
