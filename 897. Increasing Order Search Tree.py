# Problem link https://leetcode.com/problems/increasing-order-search-tree/

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def increasing_bast(self, root):
        if root is None:
            return

        self.increasing_bast(root.left)
        new_node = Node(root.val)
        self.increasing_bast(root.right)

        return new_node