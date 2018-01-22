class MyClass:
    def __call__(self):
        print('You can call cls() directly.')


cls = MyClass()
cls()

print(callable(cls))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))
