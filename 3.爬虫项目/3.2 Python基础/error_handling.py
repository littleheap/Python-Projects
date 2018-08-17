# 错误处理

try:
    r = 10 / 0
except ZeroDivisionError as e:
    print(type(e))  # <class 'ZeroDivisionError'>
    print(e)  # division by zero
finally:
    # 防止资源泄露
    print('Always come here.')  # Always come here.
