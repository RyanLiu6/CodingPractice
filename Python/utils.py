def binarySearch(nums, left, right, target):
    if right < left:
        return -1

    mid = int((left + right)/2)

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binarySearch(nums, left, mid - 1, target)
    else:
        return binarySearch(nums, mid + 1, right, target)


def QuickSelect(nums, k):
    if nums:
        pos = partition(nums, 0, len(nums) - 1)
        if k > pos + 1:
            return QuickSelect(nums[pos + 1:], k - pos - 1)
        elif k < pos + 1:
            return QuickSelect(nums[:pos], k)
        else:
            return nums[pos]


# choose the right-most element as pivot
def partition(nums, left, right):
    low = left
    while left < right:
        if nums[left] < nums[right]:
            nums[left], nums[low] = nums[low], nums[left]
            low += 1
        left += 1
    nums[low], nums[right] = nums[right], nums[low]
    return low


def MergeSort(nums):
    n = len(nums)
    if n == 1:
        return nums

    first = nums[:int(n/2)]
    second = nums[int(n/2):]

    first = MergeSort(first)
    second = MergeSort(second)

    return Merge(first, second)


def Merge(first, second):
    n1 = len(first)
    n2 = len(second)
    index1, index2 = 0, 0
    retArr = []

    while index1 < n1 and index2 < n2:
        if first[index1] < second[index2]:
            retArr.append(first[index1])
            index1 += 1
        else:
            retArr.append(second[index2])
            index2 += 1

    while index1 < n1:
        retArr.append(first[index1])
        index1 += 1

    while index2 < n2:
        retArr.append(second[index2])
        index2 += 1

    return retArr
