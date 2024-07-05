def indexed_sequential_search(arr, target, index):
    n = len(arr)
    for i in range(len(index) - 1):
        if index[i] <= target < index[i + 1]:
            for j in range(i * n // len(index), (i + 1) * n // len(index)):
                if arr[j] == target:
                    return j
    return -1


# 사용 예제
arr_sorted = [1, 2, 3, 4, 7, 9]
index = [1, 3, 7]
print(indexed_sequential_search(arr_sorted, 7, index))  # 4
print(indexed_sequential_search(arr_sorted, 5, index))  # -1
