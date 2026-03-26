# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root.left and not root.right:
                return root.val == 1
            left = dfs(root.left)
            right = dfs(root.right)
            if root.val == 2:
                return left or right
            if root.val == 3:
                return left and right
        return dfs(root)