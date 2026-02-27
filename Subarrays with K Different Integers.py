class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k_max):
            l = 0
            count = 0 
            freq = {}
            for i in range(len(nums)):
                freq[nums[i]] = freq.get(nums[i] ,0 ) + 1
            
                while len(freq) > k_max:
                    freq[nums[l]] -= 1
                    if  freq[nums[l]] == 0:
                        del freq[nums[l]] 
                    l += 1
                count += (i-l + 1)
            return count
        return atmost(k) - atmost(k-1) 
