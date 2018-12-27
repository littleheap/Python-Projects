def countdown(i):
    print(i)
    # 基线条件
    if i <= 0:
        return
    # 递归条件
    else:
        countdown(i - 1)


countdown(5)
'''
    5
    4
    3
    2
    1
    0
'''