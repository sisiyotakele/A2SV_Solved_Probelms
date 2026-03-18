class Solution:
    def numberOfSteps(self, num: int) -> int:
        def pro(n):
            
            if n == 0:
                return 0
            if n %2 == 0:
                return 1 +pro(n//2)
            else:
                return 1 + pro(n-1)
        return pro(num)