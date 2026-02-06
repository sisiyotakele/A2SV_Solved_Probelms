class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c  = Counter(nums)
        res= []
        n = len(nums)
        print(c)
        for i in c:
            print(i)
            if c[i] > math.floor(n/3):
                res.append(i)

        return res
