class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        dub_num = 0 
        n= len(nums)
        for i in nums:
            if freq[i] == 2:
                dup_num = i
        exp_sum = n * (n + 1) // 2
        miss_num = exp_sum -(sum(nums) - dup_num)
        return [dup_num , miss_num]