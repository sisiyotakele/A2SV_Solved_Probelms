# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(nums):
            if not nums:
                return None
            idx = nums.index(max(nums))
            root = TreeNode(nums[idx])
            
            root.left = dfs(nums[:idx])
            root.right = dfs(nums[idx+1:])
            
            return root
        
        return dfs(nums)

