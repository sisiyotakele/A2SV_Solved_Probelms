class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq=Counter(nums)
        res=[]
        for n in freq:
            if freq[n] > 1:
                res.append(n)
        return res
