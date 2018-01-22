# 描述器：实现了__set__/__get__/__del__方法的类
class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        print("__init__")
        print(fget)
        print(fset)
        print(fdel)
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, cls):
        if self.fget:
            print('__get__')
            return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset:
            print('__set__')
            return self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel:
            print("__delete__")
            return self.fdel(instance)

    def getter(self, fn):
        print("getter")
        self.fget = fn

    def setter(self, fn):
        print("setter")
        self.fset = fn

    def deler(self, fn):
        print("deler")
        self.fdel = fn


class Student:
    @MyProperty
    def score(self):
        print("1")
        return self._score

    @score.setter
    def set_score(self, value):
        print("2")
        self._score = value


s = Student()
s.score = 95
print(s.score)
