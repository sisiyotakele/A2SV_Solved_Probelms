# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                return False
            if (k - node.val) in res:
                return True
            res.append(node.val)
            left = dfs(node.left)
            right = dfs(node.right) 
            return left or right
        return dfs(root)           