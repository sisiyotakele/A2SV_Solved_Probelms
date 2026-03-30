# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0
        def dfs (node):
            nonlocal moves
            if not node:
                return 0
            left_bal = dfs(node.left)
            right_bal = dfs(node.right)
            
            moves += abs(left_bal) + abs(right_bal)

            curr_bal = node.val - 1

            return curr_bal + left_bal + right_bal
        dfs(root)
        return moves