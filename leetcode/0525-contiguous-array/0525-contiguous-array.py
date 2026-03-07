class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        his = {0: -1}
        curr_sum = 0
        max_len = 0 
        for i in range(len(nums)) :
            if nums[i] == 1:
                curr_sum += 1
            else:
                curr_sum -= 1
            if curr_sum in his:
                past_idx = his[curr_sum]
                length = i - past_idx
                max_len = max(max_len,length)
            else:
                his[curr_sum] = i
        return max_len