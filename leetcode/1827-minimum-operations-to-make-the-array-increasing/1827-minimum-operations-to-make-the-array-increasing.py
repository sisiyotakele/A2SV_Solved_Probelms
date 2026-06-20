class Solution:
    def minOperations(self, nums: List[int]) -> int:
        opr = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                needed = nums[i - 1] + 1
                opr += needed - nums[i]
                nums[i] = needed

        return opr