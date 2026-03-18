class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        def choose(nums,l,r,n):
            
            if l == r:
                return nums[l]
            left_score  = nums[l] - choose(nums,l+1,r,n) 
            right_score  = nums[r] - choose(nums, l,r-1,n)
            return max(left_score,right_score)
            
        res=  choose(nums,0,n-1,n)
        if res >= 0:
            return True
        else:
            return False
            
        
