class Fib:
    def __getitem__(self, n):
        print(type(n))
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a


f = Fib()
print(f[1])
print(f[5])
print(f[10])
# print(f[1:2:3])
