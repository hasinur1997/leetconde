class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value

        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
            return

        if len(self.cache) >= self.capacity:
            least_used_key = next(iter(self.cache))
            self.cache.pop(least_used_key)

        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.get(2)

obj.put(2, 1)
obj.put(1, 1)
obj.put(2, 3)
obj.put(4, 1)

print(obj.cache)


print(obj.get(1))
print(obj.get(2))


