# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        def current_path(node,rem):
            nonlocal count
            if not node:
                return 0
            rem -= node.val
            if rem == 0:
                count += 1
            current_path(node.left,rem)
            current_path(node.right,rem)
            
        def traverse(node):
            if not node:
                return 0
            current_path(node, targetSum)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return count
            
            

            