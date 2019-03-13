# input()函数
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

'''
    Tell me something, and I will repeat it back to you:
    Enter 'quit' to end the program. a
    a
    
    Tell me something, and I will repeat it back to you:
    Enter 'quit' to end the program. s
    s
    
    Tell me something, and I will repeat it back to you:
    Enter 'quit' to end the program. d
    d
    
    Tell me something, and I will repeat it back to you:
    Enter 'quit' to end the program. q
    q
    
    Tell me something, and I will repeat it back to you:
    Enter 'quit' to end the program. quit
    
    Process finished with exit code 0
'''