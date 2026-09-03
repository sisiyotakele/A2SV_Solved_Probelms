class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')

        for x in nums1:
            if x % 2 == 1:
                min_odd = min(min_odd, x)
        can_odd = True

        for x in nums1:
            if x % 2 == 0 and min_odd >= x:
                can_odd = False
                break

        if can_odd:
            return True

        can_even = True

        for x in nums1:
            if x % 2 == 1 and min_odd >= x:
                can_even = False
                break

        return can_even