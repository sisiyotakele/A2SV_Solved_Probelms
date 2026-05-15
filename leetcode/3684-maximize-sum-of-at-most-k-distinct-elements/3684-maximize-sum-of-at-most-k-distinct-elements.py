class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort(reverse=True)

        res = []

        for i in nums:
            if i not in res:
                res.append(i)

        return res[:k]