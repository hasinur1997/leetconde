# Problem Link https://leetcode.com/problems/linked-list-cycle/
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):
    if head is None:
        return False

    current = head
    visited = []

    while current is not None:
        if current.next in visited:
            return True
        visited.append(current)
        current = current.next

    return False




node1 = Node(3)
node2 = Node(2)
node3 = Node(0)
node4 = Node(4)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(has_cycle(head))
