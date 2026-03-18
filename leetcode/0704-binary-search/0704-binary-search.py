class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1
        
        def choose (l ,r):
            if l > r :
                return -1
            mid = (l + r) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return choose(mid+1,r)
            else:
                return choose(l,mid-1)
        return choose(0,len(nums) -1)