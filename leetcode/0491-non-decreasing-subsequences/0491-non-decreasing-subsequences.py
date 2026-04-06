class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i,curr):
            if i == len(nums):
                if len(curr) >= 2 and curr not in res:
                    res.append(curr[:])
                return
            used = set()
            if (not curr or nums[i] >= curr[-1]) and nums[i] not in used:
                used.add(nums[i])
                #take
                backtrack(i+1,curr + [nums[i]])

            # notake
            backtrack (i + 1 , curr)
        backtrack(0, [])
        return res