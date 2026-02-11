class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        total_count = Counter(nums)
        m = total_count.most_common(1)[0][0]
        total_m = total_count[m]
        
        left_count = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] == m:
                left_count += 1
            
            right_count = total_m - left_count
            
            if left_count > (i + 1) // 2 and right_count > (n - i - 1) // 2:
                return i
        
        return -1
