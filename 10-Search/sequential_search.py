def sequential_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


# 사용 예제
arr = [4, 2, 7, 1, 9, 3]
print(sequential_search(arr, 7))  # 2
print(sequential_search(arr, 5))  # -1
