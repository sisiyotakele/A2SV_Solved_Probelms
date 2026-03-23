class Solution:
    def trailingZeroes(self, n: int):   
        
        def factorial(num):
            if num == 0 or num == 1:
                return 1
            return num * factorial(num - 1)     
        
        res = factorial(n)

        count = 0
        while res % 10 == 0:
            count += 1
            res //= 10
        
        return count