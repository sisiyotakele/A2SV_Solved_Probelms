class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        count_map = {}
        for i, num in enumerate(sorted_nums):
            if num not in count_map:
                count_map[num] = i
        result = [count_map[num] for num in nums]
        return result
