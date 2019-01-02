def quicksort(array):
    if len(array) < 2:
        # 基线条件：数列为空或者只包含一个元素的数组一定是有序的
        return array
    else:
        # 递归条件：基准值直接取每组自数列的首个元素
        pivot = array[0]
        # 由所有小于等于基准值的元素组成的子数组
        less = [i for i in array[1:] if i <= pivot]
        # 由所有大于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))  # [2, 3, 5, 10]
