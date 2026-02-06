class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict ={}
        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) + 1
        for j in nums_dict:
            if nums_dict[j] == 1:
                return j
