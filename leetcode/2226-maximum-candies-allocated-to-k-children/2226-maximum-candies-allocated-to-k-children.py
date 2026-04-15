class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1 , max(candies)
        ans = 0 
        while l <= r:
            mid = (l+r) // 2
            tot_child = 0
            for i in range(len(candies)):
                tot_child += candies[i] // mid
            if tot_child >= k:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
