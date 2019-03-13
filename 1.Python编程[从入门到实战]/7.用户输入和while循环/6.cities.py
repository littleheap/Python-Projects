# break退出循环
prompt = "\nPlease tell me a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

'''
    Please tell me a city you have visited:
    (Enter 'quit' when you are finished.) New York
    I'd love to go to New York!
    
    Please tell me a city you have visited:
    (Enter 'quit' when you are finished.) quit
    
    Process finished with exit code 0
'''