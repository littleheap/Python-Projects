def move(n, source, target, helper):
    if n == 1:
        print(source + ' -> ' + target)
    else:
        move(n - 1, source, helper, target)
        print(source + ' -> ' + target)
        move(n - 1, helper, target, source)


move(4, 'A', 'B', 'C')

'''
A -> C: [2, 3, 4], [], [1]
A -> B: [3, 4], [2], [1]
C -> B: [3, 4], [1, 2]
A -> C: [4], [1, 2], [3]
B -> A: [1, 4], [2], [3]
B -> C: [1, 4], [], [2, 3]
A -> C: [4], [], [1, 2, 3]
A -> B: [], [4], [1, 2, 3]
C -> B: [], [1, 4], [2, 3]
C -> A: [2], [1, 4], [3]
B -> A: [1, 2], [4], [3]
C -> B: [1, 2], [3, 4], []
A -> C: [2], [3, 4], [1]
A -> B: [], [2, 3, 4], [1]
C -> B: [], [1, 2, 3, 4], []
'''
