a = 1234
print(a)
a = 'abcd'
print(a)

try:
    print(b)
except Exception as e:
    print(e)

a = [1, 2, 3 , 4]

def func(a):
    a[0] = 2

func(a)
print(a)

try:
    # Python 2.x 支持
    print 100, 200, 300
except Exception as e:
    print(e)
