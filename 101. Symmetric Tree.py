# Problem Link https://leetcode.com/problems/symmetric-tree/
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_symentric(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1.val == root2.val:
        return is_symentric(root1.left, root2.right) and is_symentric(root1.right, root2.left)

    return False


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node4 = TreeNode(5)
node5 = TreeNode(4)
node6 = TreeNode(4)
node7 = TreeNode(3)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

print(is_symentric(node1, node1))
