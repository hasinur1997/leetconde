# Problem Link https://leetcode.com/problems/range-sum-of-bst/
def pre_order(node):
    if node is None:
        return

    print(node.data)
    pre_order(node.left)
    pre_order(node.right)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:

    def range_sum_bst(self, root, low, high):
        return self.bst_sum(root, low, high)


    def bst_sum(self, root, low, high):
        if root is None:
            return 0

        value = 0

        if root.data >= low and root.data <= high:
            value = root.data

        return value + self.bst_sum(root.left, low, high) + self.bst_sum(root.right, low, high)


    def get_sum(self, root):
        if root is None:
            return 0

        return root.data + self.get_sum(root.left) + self.get_sum(root.right)


root = Node(10)

root.left = Node(5)
root.right = Node(15)

root.left.left = Node(3)
root.left.right = Node(7)

root.right.right = Node(18)

st = Solution()

print(st.bst_sum(root, 7, 15))

# pre_order(root)
