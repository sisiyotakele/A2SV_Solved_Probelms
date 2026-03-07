class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int :
        his = defaultdict(int)
        his[0] = 1 
        curr_sum = 0
        total = 0
        for num in nums:
            curr_sum += num
            remainder = curr_sum % k
            
            total += his[remainder]

            his[remainder] += 1
        return total

            

