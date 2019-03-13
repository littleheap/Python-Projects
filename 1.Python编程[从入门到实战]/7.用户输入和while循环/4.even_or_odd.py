# 判断输入奇数偶数
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
'''
    Enter a number, and I'll tell you if it's even or odd: 11
    
    The number 11 is odd.
'''