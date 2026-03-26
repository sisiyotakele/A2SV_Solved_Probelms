# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(root,res):
            # res = ''
            if not root :
                return
            res += str(root.val)
            if not root.left and not root.right:
                ans.append(res)
            dfs(root.left,res+ "->")
            dfs(root.right, res + "->")
        dfs(root,"")
        return ans