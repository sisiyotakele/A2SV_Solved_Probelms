class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        diff = [0] *(n+1)

        for l,r in requests:
            diff[l] += 1
            diff[r+1] -= 1
        freq =[0]*n
        curr = 0
        for i in range(n):
            curr += diff[i]
            freq[i] = curr
        freq.sort()
        nums.sort()
        mod = 10**9 +7
        max_sum = 0
        for i in range(n):
            max_sum = (max_sum + freq[i] * nums[i]) % mod
        return max_sum


             

       

