class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, cur):
            if len(cur) == k:
                res.append(cur[::])
                return
            if i > n:
                return
            
            # take
            backtrack(i + 1, cur + [i])
            # not take
            backtrack(i + 1, cur)
        backtrack(1, [])
        return res