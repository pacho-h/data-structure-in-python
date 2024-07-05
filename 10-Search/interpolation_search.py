def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        pos = low + ((high - low) // (arr[high] - arr[low]) * (target - arr[low]))

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1


# 사용 예제
arr_sorted = [1, 2, 3, 4, 7, 9]
print(interpolation_search(arr_sorted, 7))  # 4
print(interpolation_search(arr_sorted, 5))  # -1
