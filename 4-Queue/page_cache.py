from collections import deque


class PageCache:
    def __init__(self, capacity):
        self.queue = deque()
        self.capacity = capacity

    def access_page(self, page):
        if page in self.queue:
            self.queue.remove(page)
        elif len(self.queue) >= self.capacity:
            self.queue.popleft()
        self.queue.append(page)

    def get_cache(self):
        return list(self.queue)


# 사용 예제
page_cache = PageCache(3)
page_cache.access_page(1)
page_cache.access_page(2)
page_cache.access_page(3)
print(page_cache.get_cache())  # [1, 2, 3]
page_cache.access_page(4)
print(page_cache.get_cache())  # [2, 3, 4]
page_cache.access_page(2)
print(page_cache.get_cache())  # [3, 4, 2]
