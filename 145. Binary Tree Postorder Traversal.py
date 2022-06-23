# Problem link https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def postorderTraversal(self, root):
        ans = []

        def post_order(root):
            if root is None:
                return

            post_order(root.left)
            post_order(root.right)
            ans.append(root.val)

        post_order(root)

        return ans