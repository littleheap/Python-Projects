with open('text.txt') as f:
    for line in f.readlines():
        print(line)
'''
    1234
    
    abcd
    
    efgh
'''

with open('text.txt', 'rb') as f:
    print(f.read())
# b'1234\r\nabcd\r\nefgh'
