class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        res=[]
        nums.sort()
        for i in range(1,len(nums)):
            res.append(abs(nums[i] - nums[i-1]))
        
        return  max(res)

