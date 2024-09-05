# 归并排序的实现
def merge_sort(arr):
    # 如果数组的长度小于等于1，直接返回（递归的基线条件）
    if len(arr) <= 1:
        return arr
    
    # 找到数组的中间位置
    mid = len(arr) // 2
    
    # 递归地对左半部分进行排序
    left_half = merge_sort(arr[:mid])
    
    # 递归地对右半部分进行排序
    right_half = merge_sort(arr[mid:])
    
    # 合并已经排序的两部分
    return merge(left_half, right_half)

# 合并两个已经排序的数组
def merge(left, right):
    result = []  # 存储最终合并的结果
    i = 0  # 指向左半部分的指针
    j = 0  # 指向右半部分的指针
    
    # 当左右两部分都有元素时，比较并按顺序放入结果数组
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])  # 左半部分的元素较小，放入结果
            i += 1  # 左半部分指针向右移动
        else:
            result.append(right[j])  # 右半部分的元素较小，放入结果
            j += 1  # 右半部分指针向右移动
    
    # 如果左半部分还有剩余元素，全部加入结果
    result.extend(left[i:])
    
    # 如果右半部分还有剩余元素，全部加入结果
    result.extend(right[j:])
    
    return result  # 返回合并后的数组

# 测试归并排序
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("排序后的数组:", sorted_arr)

##########################################
#`代码解释：
#merge_sort(arr) 是递归函数，负责将数组拆分成越来越小的子数组，直到每个子数组的长度为1或0。
#merge(left, right) 函数负责合并两个已排序的子数组，比较它们的第一个元素并按顺序合并成一个大的有序数组。
#每次递归都会将数组分为左右两部分，最后利用 merge 将它们合并。
