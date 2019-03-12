# 字典基础用法
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original position: " + str(alien_0['x_position']))
# Original position: 0

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New position: " + str(alien_0['x_position']))
# New position: 2

# 删除键
del alien_0['speed']
print(alien_0)
# {'x_position': 2, 'y_position': 25}
