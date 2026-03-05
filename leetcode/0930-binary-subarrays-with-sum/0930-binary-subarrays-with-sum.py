class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref_history= {}
        pref_history[0] = 1
        curr_sum = 0
        total_sum = 0
        for num in nums:
            curr_sum += num
            needed_sum = curr_sum - goal

            if needed_sum in pref_history:
                total_sum  += pref_history[needed_sum]
            pref_history[curr_sum] = pref_history.get(curr_sum , 0) +1
            
        return total_sum

