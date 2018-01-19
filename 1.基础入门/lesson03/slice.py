li = list(range(10))
print(li)

# 切片 [start:end:steps]  >= start & < end
print(li[2:5])  # [3, 4, 5]
print(li[:4])  # [0, 1, 2, 3]
print(li[5:])  # [6, 7, 8, 9]
print(li[0:20:3])  # [0, 3, 6, 9]

# 负值处理
print(li[5: -2])  # [5, 6, 7]
print(li[9:0:-1])  # [9, 8, 7, 6, 5, 4, 3, 2,1]
print(li[9::-1])  # [9 ... 0]
print(li[::-2])  # [9, 7, 5, 3, 1]

# 切片生成一个新的对象
print(li)  # 还是保持原样

re_li = li[::-1]
print(re_li)
