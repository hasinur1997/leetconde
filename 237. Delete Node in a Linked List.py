class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:
    def delete_node(self, node):
        node.val = node.next.val
        node.next = node.next.next
