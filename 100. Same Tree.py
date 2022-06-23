# Problem Link https://leetcode.com/problems/same-tree/
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs(root):
    data = []

    qu = [root]

    while qu:
        node = qu.pop()
        data.append(node.val)

        if node.right:
            qu.append(node.right)

        if node.left:
            qu.append(node.left)

    return data


def is_same_tree(p, q):
    # return bfs(p) == bfs(q)
    if p is None:
        return q is None

    if q is None:
        return False

    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Make tree
node1.left = node2
node1.right = node3

root1 = node1
root2 = node1










# print(is_same_tree(root1, root2))

print([1,2] == [1,'null',2])