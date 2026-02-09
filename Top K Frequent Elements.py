class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        lst=Counter(nums)
        sorted_c = sorted(lst.items(), key=lambda x: x[1], reverse=True)
        return [key for key, value in sorted_c[:k]]
