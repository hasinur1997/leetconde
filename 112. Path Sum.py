# Problem Link https://leetcode.com/problems/path-sum/

def has_path_sum(root, targetSum):

    def solve(node, target, s):

        if not node:
            return False

        if node.left is None and node.right is None:
            s += node.val
            return target == s

        return solve(node.left, target, s) or solve(node.right, target, s)

    return solve(root, targetSum, 0)
