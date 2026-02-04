class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        exp_sum = n*(n+1)//2
        act_sum = sum(nums)
        return exp_sum - act_sum
        # for i in range(0,n+1):
        #     if i not in nums:
        #         return i  NOT OPTIMAL
