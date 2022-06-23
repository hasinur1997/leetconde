# Problem Link https://leetcode.com/problems/palindrome-linked-list/
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def is_palindrome(head):
    if head is None:
        return False

    values = []
    rev = []
    current = head

    while current is not None:
        values.append(current.val)
        current = current.next

    rev = [item for item in values]
    rev.reverse()

    return rev == values


node1 = Node(1)
node2 = Node(2)

node1.next = node2

print(is_palindrome(node1))
