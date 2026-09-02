class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        has_odd = any(x % 2 for x in nums1)
        has_even = any(x % 2 == 0 for x in nums1)

        return not (has_odd and has_even) or len(nums1) > 1