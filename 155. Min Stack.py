# Problem Link https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self):
        self.index = -1
        self.data = []

    def push(self, val):
        self.data.append(val)
        self.index += 1

    def pop(self):
        self.data.pop()
        self.index -= 1

    def top(self):
        return self.data[self.index]

    def get_min(self):
        return min(self.data)



min_stack = MinStack()

min_stack.push(10)
min_stack.push(20)
min_stack.push(50)

# print(min_stack.pop())
print(min_stack.get_min())