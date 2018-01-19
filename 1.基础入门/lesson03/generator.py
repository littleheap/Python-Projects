print(type(range(10)))

# 平方表
square_table = []
for i in range(5000):
    square_table.append(i * i)
for i in range(5):
    print(square_table[i])

# 用到了才计算，不用到不计算
square_generator = (x * x for x in range(100))
print(type(square_generator))
print(square_generator)
for i in range(5):
    print(next(square_generator))


def fib(limit):
    n, a, b = 0, 0, 1
    while n < limit:
        # 执行完yield返回后不动，等待下一个next指令才继续执行
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


import traceback

f = fib(5)

print("...")
print(type(f))
print(next(f))  # 1
print(next(f))  # 1
print(next(f))  # 2
print(next(f))  # 3
print(next(f))  # 5

try:
    print(next(f))
except StopIteration:
    traceback.print_exc()

for i in fib(5):
    print(i)
