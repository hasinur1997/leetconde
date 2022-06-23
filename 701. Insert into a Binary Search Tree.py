# Problem link https://leetcode.com/problems/insert-into-a-binary-search-tree/

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def pre_order(root):
    if root is None:
        return

    print(root.val)
    pre_order(root.left)
    pre_order(root.right)


def insert(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root


node1 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(7)
node4 = TreeNode(1)
node5 = TreeNode(3)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5
insert(node1, 5)

pre_order(node1)
