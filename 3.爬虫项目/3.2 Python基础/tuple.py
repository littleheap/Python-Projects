# 只读数组
tp = (1, 2, 3)

try:
    tp[0] = 100
except Exception as e:
    print(e)  # 'tuple' object does not support item assignment
