import traceback


class Student:
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        # 类型检查，是否为int
        if not isinstance(value, int):
            raise ValueError('not int')

        elif (value < 0) or (value > 100):
            raise ValueError('not between 0 ~ 100')

        self._score = value

    # 此属性只有property，没有setter，所以只能读不能写
    @property
    def double_score(self):
        return self._score * 2


s = Student()
s.score = 75
print(s.score)
try:
    s.score = 'abc'
except ValueError:
    traceback.print_exc()
try:
    s.score = 101
except:
    traceback.print_exc()
print(s.double_score)
try:
    s.double_score = 150
except AttributeError:
    traceback.print_exc()
