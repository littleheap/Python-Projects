# 找到数列中最小的元素
def findSmallest(arr):
    # 存储当前遍历到的最小元素
    smallest = arr[0]
    # 存储当前最小元素的索引
    smallest_index = 0
    # 如果找到更小元素，则更新最小元素信息
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
    # 返回查找到的最小元素索引
    return smallest_index


# 数列排序
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        # 找到当前数列最小元素并放到一个新数列存储器中
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


# 选择排序从小到大排序数列
print(selectionSort([5, 3, 6, 2, 10]))
# [2, 3, 5, 6, 10]
