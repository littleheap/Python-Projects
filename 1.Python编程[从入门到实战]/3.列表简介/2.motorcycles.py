# 修改，添加和删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
# ['honda', 'yamaha', 'suzuki', 'ducati']

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
# ['honda', 'yamaha', 'suzuki']

print("\nA " + too_expensive.title() + " is too expensive for me.")
# A Ducati is too expensive for me.

# 添加元素
motorcycles.append('ducati')
print(motorcycles)
# ['honda', 'yamaha', 'suzuki', 'ducati']

# 插入元素
motorcycles.insert(0, 'bmw')
print(motorcycles)
# ['bmw', 'honda', 'yamaha', 'suzuki', 'ducati']

# 删除元素
del motorcycles[0]
print(motorcycles)
# ['honda', 'yamaha', 'suzuki', 'ducati']

# pop()删除元素
motorcycles.pop()
print(motorcycles)
# ['honda', 'yamaha', 'suzuki']

# remove()删除元素
motorcycles.remove('honda')
print(motorcycles)
# ['yamaha', 'suzuki']
