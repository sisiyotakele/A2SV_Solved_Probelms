# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        def calc(level):
            ans = 0
            srt = sorted(level)
            mp = defaultdict(int)
            for i, num in enumerate(level):
                mp[num] = i
                
            for i, cur in enumerate(level):
                swap = 0
                cur = i
                while level[cur] != srt[cur]:
                    temp = mp[srt[cur]]
                    level[cur], level[mp[srt[cur]]] = level[mp[srt[cur]]], level[cur]
                    cur = temp
                    swap += 1
                ans += swap
            return ans

        ans = 0
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans += calc(level)
        return ans