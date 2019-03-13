# 使用用户输入建立字典
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

'''
    What is your name? Wang
    Which mountain would you like to climb someday? Tai
    Would you like to let another person respond? (yes/ no) no
    
    --- Poll Results ---
    Wang would like to climb Tai.
'''
