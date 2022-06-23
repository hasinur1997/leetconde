# Problem Link https://leetcode.com/problems/sort-list/

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:
    def sort(self, head):
        if head is None:
            return head

        current = head

        while current is not None:
            p = current

            while p is not None:
                if p.value < current.value:
                    p.value, current.value = current.value, p.value
                p = p.next

            current = current.next

        return head


node1 = Node(90)
node2 = Node(20)
node3 = Node(102)
node4 = Node(43)

node1.next = node2
node2.next = node3

node3.next = node4

solution = Solution()
head = solution.sort(node1)

current = head

while current is not None:
    print(current.value)
    current = current.next



