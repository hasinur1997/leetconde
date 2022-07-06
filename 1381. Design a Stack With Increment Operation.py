class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [] * maxSize
        self.size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) >= self.size:
            return
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(len(self.stack[:k])):
            self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(3)
obj.push(1)
obj.push(2)
obj.pop()
obj.push(2)
obj.push(3)
obj.push(4)
obj.increment(5, 100)
obj.increment(2, 100)
obj.pop()
obj.pop()
obj.pop()


print(obj.pop())