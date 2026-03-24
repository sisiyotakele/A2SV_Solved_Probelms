# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = -inf
        def dfs(node):
            nonlocal prev
            if not node:
                return True
            left = dfs(node.left)
            if node.val <= prev:
                return False
            prev = node.val
            right = dfs(node.right)
            return left and right
        return dfs(root)