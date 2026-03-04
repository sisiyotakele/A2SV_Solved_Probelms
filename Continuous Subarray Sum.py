class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen_rem = {0:-1}
        running_sum = 0

        for i in range(len(nums)):
            running_sum += nums[i]
            reminder = running_sum % k 

            if reminder not in seen_rem:
                seen_rem[reminder] = i
            else:
                if i - seen_rem[reminder] >= 2:
                    return True
        return False
