def binary_search(list, item):
    # low和high两个游标记录要搜索的范围边界
    low = 0
    high = len(list) - 1

    # 当算法不断二分并缩小搜索范围
    while low <= high:
        # 检查目标范围内二分点中间元素是否为查找对象
        mid = (low + high) // 2
        guess = list[mid]
        # 如果找到目标元素
        if guess == item:
            return mid
        # 当中间元素大于目标元素
        if guess > item:
            high = mid - 1
        # 如果中间元素小于目标元素
        else:
            low = mid + 1

    # 搜索范围越界则说明没有目标元素
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))  # => 1

# None代表数列中没有目标元素
print(binary_search(my_list, -1))  # => None
