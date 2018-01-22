try:
    # r = 10 / 0
    r = 10 / 1
except ZeroDivisionError as e:
    print(e)
    r = 1
else:
    print('没有异常')
finally:
    print('不管有没有异常都执行')
print(r)
