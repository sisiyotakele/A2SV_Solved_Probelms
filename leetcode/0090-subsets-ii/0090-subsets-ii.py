class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  
        
        n = len(nums)
        
        def backtrack(i, curr):
            if i == n: 
                res.append(curr[:])  
                return
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop() 
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1  
            
            backtrack(i + 1, curr)
        
        backtrack(0, [])
        return res
