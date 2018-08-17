score = 80

if score > 90:
    print('A')
elif score > 70:
    print('B')  # B
elif score >= 60:
    print('C')
else:
    print('D')

total = 0

i = 1

while i <= 100:
    total += i
    i += 1  # 没有++i或者--i

print(total)  # 5050

i = 0

while i < 3:
    j = 0
    while j <= 3:
        if j == 2:
            j += 1
            continue
        print(i, j)
        j += 1
    i += 1
'''
    0 0
    0 1
    0 3
    1 0
    1 1
    1 3
    2 0
    2 1
    2 3
'''
