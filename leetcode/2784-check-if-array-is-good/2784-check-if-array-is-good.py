class Solution:
    def isGood(self, nums: List[int]) -> bool:
        max_elm = max(nums)
        if len(nums) < max_elm + 1 or len(nums) > max_elm + 1:
            return False
        count = Counter(nums)
        if count[max_elm] != 2:
            return False
        for i in range(1,len(nums) - 1):
            if i not in nums or count[i] != 1:
                return False
        return True