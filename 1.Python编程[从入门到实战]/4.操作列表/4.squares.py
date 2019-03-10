# 处理平方运算
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 列表解析写法
new_squares = [value ** 2 for value in range(1, 11)]
print(new_squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
