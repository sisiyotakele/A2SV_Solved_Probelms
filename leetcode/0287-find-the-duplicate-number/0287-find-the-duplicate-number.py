class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l , r = 0 , len(nums) - 1
        
        while l < r:
            count = 0
            mid = (l+r) // 2
            for num in nums:
                if num <= mid :
                    count += 1
            if count > mid:
                r = mid
            else:
                l = mid + 1
        return l 
