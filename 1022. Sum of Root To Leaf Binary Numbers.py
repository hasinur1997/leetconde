# Problem Link https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def pre_order(root):
    if root is None:
        return
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)


root = Node(10)

node1 = Node(5)
node2 = Node(10)
node3 = Node(50)
node4 = Node(54)
node5 = Node(90)

root.left = node1
root.right = node2

node1.left = node3
node1.right = node4

node4.left = node5

pre_order(root)
