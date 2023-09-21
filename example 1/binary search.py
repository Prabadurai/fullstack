def binary_search(n, item):
    left, right= 0, len(n)
    while right > left:
        middle = (left + right) // 2
        if nums[middle] > item:
            right = middle
        elif nums[middle] < item :
            left = middle + 1
        else:
            return middle
    return None