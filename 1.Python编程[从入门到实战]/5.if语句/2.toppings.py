# 检查是否相等
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
'''
    Adding mushrooms.
    Sorry, we don't have french fries.
    Adding extra cheese.
'''

print("\nFinished making your pizza!")
# Finished making your pizza!
