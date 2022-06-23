# Problem Link https://leetcode.com/problems/sum-of-left-leaves/

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_leaf(node):
    if node is None:
        return False

    if node.left is None and node.right is None:
        return True

    return False


def sum_left_leaves(root):
    if root.left is None:
        return 0

    res = 0

    if is_leaf(root.left):
        res += root.left.val
    else:
        res += sum_left_leaves(root.left)

    res += sum_left_leaves(root.right)

    return res


def get_data(node, data=[]):
    if node is None:
        return

    data.append(node.val)
    get_data(node.left, data)
    get_data(node.right, data)

    return data

node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node1.left = node2
node1.right = node3

node3.left = node4
node3.right = node5


print(get_data(node1))
