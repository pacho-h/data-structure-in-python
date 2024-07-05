import heapq


def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr


arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(heap_sort(arr))  # [1, 1, 2, 3, 4, 5, 5, 6, 9]
