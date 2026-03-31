class Solution:
    def mySqrt(self, x: int) -> int:
        # def choose (l,r):
        l = 1
        r = x
        if x == 0:
            return 0 
        while l <= r:
            mid  = (l +  r) // 2 
            print(mid)
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
        return r