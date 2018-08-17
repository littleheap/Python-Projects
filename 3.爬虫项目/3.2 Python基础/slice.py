# [1, 2, 3, 4, 5]
#  => [1, 2, 3]
#  => [3, 4]
li = [1, 2, 3, 4, 5]
li_0_2 =li[0:3] # 0 <= ? < 3
# 等价li[:3]
print(li_0_2)
# [start, end, step] => [start, start + step, ..., < end]
# start默认是0，end默认-1，step默认1
li_last_3 = li[-1:-4:-1]
print(li_last_3)

# 直接用切片反转数组
print(li[::-1])
print(li[-2::-1])

# 切片是复制
li_0_2[-1] = 100
print(li)
