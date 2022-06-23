# Problem Link https://leetcode.com/problems/implement-queue-using-stacks/

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, item):
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(item)

        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())

    def pop(self):
        if self.is_empty():
            return False
        return self.stack1.pop()

    def peek(self):
        if self.is_empty():
            return False
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) < 1



q = Queue()
q.push(10)
q.push(20)
q.push(30)
q.push(40)
q.push(50)
q.push(60)

print(q.stack1)
print(q.pop())
print(q.is_empty())
