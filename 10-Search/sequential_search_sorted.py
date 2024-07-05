def sequential_search_sorted(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
        elif value > target:
            break
    return -1


# 사용 예제
arr_sorted = [1, 2, 3, 4, 7, 9]
print(sequential_search_sorted(arr_sorted, 7))  # 4
print(sequential_search_sorted(arr_sorted, 5))  # -1
