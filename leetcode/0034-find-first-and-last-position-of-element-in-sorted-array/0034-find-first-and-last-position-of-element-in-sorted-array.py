class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res= [-1,-1]
        k = 0
        for i in range(len(nums)):
            if nums[i] == target:
                res[0] = i
                k= i
                break
        for j in range(k,len(nums)):
            if nums[j] == target:
                res[1] = j
                
        return res