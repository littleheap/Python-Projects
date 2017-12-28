# if判断
a = 100
b = 200
c = 300
if c == a:
    print(a)
elif c == b:
    print(b)
else:
    print(c)

# None的判断
x = None
if x is None:
    print('x is None')
if not x:
    print('x is None')

# for循环
s = 0
for i in range(0, 101):
    s += i
print(s)

# while循环
s = 0
i = 0
while i <= 100:
    s += i
    i += 1
print(s)

# continue/pass/break
for i in range(0, 100):
    if i < 10:
        pass
    elif i < 30:
        continue
    elif i < 35:
        print(i)
    else:
        break
