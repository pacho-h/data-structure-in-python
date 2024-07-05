def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# 사용 예제
arr_sorted = [1, 2, 3, 4, 7, 9]
print(binary_search(arr_sorted, 7))  # 4
print(binary_search(arr_sorted, 5))  # -1
