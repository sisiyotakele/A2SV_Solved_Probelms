class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r= 1,sum(piles)
        def speed(mid):
            hrs = 0
            for p in piles:
                hrs += math.ceil(p/mid)
                if hrs > h:
                    return False
            return True
        while l <= r:
            mid = (l + r) //2
            if speed(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

        