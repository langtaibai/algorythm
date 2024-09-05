def quicksort(arr, left, right):
    if left < right:
        # 获取分区点（pivot 的索引）
        pivot_index = partition(arr, left, right)
        
        # 对分区的左右两侧递归排序
        quicksort(arr, left, pivot_index - 1)
        quicksort(arr, pivot_index + 1, right)

def partition(arr, left, right):
    # 选取最右边的元素作为 pivot
    pivot = arr[right]
    i = left - 1  # 小于 pivot 元素的边界
    
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # 交换
        
    # 将 pivot 放到正确位置
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

# 测试用例
arr = [3, 6, 8, 10, 1, 2, 1]
quicksort(arr, 0, len(arr) - 1)
print(arr)  # 输出 [1, 1, 2, 3, 6, 8, 10]
#解释：
#quicksort(arr, left, right) 是主函数，它递归地对数组的左右两部分进行排序。
#partition(arr, left, right) 是核心步骤，它将数组按基准元素分为两部分，小于等于基准的在左，大于基准的在右。
#时间复杂度： 平均 O(n log n)，最坏情况 O(n²)。
#空间复杂度： 递归深度为 O(log n)
