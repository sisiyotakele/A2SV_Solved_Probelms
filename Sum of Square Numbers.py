class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=0
        b=int(math.sqrt(c))
        
        while a <= b:
            total = a*a + b*b
            if c==total:
                return True
            elif total < c:
                a +=1
            else:
                b-=1
        return False

        
