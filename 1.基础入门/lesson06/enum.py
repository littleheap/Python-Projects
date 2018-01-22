from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

jan = Month.Jan
print(jan)
