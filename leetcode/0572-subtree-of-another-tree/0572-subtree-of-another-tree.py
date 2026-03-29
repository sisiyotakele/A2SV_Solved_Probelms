# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def subtree(root,subRoot):
            if not root:
                return False
            if sametree(root,subRoot):
                return True
            return (subtree(root.left,subRoot) or subtree(root.right,subRoot))
        
        def sametree(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return (sametree(p.left,q.left) and sametree(p.right,q.right))
        return subtree(root,subRoot)
