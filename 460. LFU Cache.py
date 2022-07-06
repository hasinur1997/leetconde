# Problem Link https://leetcode.com/problems/lfu-cache/

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.cache_counter = {}

    def get(self, key):
        self.count_cache(key)
        if key in self.cache:
            return self.cache[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            self.cache[key] = value
            self.count_cache(key)
            return

        if len(self.cache) >= self.capacity:
            least_frequent_used_key = min(self.cache_counter, key=self.cache_counter.get)
            # self.cache_counter.pop(least_frequent_used_key)
            self.cache.pop(least_frequent_used_key)

        self.cache[key] = value
        self.count_cache(key)

    def count_cache(self, key):
        if key in self.cache_counter:
            self.cache_counter[key] += 1
        else:
            self.cache_counter[key] = 1

# Your LFUCache object will be instantiated and called as such:
obj = LFUCache(2)
obj.get(2)
obj.put(1, 1)
obj.put(2, 2)
obj.get(1)
obj.put(3, 3)
obj.get(2)
obj.get(3)
obj.put(4, 4)
obj.get(1)
obj.get(3)
obj.get(4)
print(obj.cache)
print(obj.cache_counter)
print(obj.get(4))

