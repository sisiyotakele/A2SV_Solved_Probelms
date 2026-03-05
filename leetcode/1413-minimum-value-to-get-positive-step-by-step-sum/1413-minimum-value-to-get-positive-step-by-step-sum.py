class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        pref_sum = [0] * (n+1)
        for i in range(n):
            pref_sum [i+1] = pref_sum[i] + nums[i]
        min_elem = min(pref_sum)
        return max(1,(1-min_elem))