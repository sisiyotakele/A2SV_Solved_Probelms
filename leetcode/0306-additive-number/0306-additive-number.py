class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        for i in range(1, n):
            for j in range(i+1, n):
                
                a = num[:i]
                b = num[i:j]
                
                # skip leading zeros
                if (a[0] == '0' and len(a) > 1) or (b[0] == '0' and len(b) > 1):
                    continue
                
                if self.valid(a, b, num[j:]):
                    return True
        
        return False
    
    def valid(self, a, b, remaining):
        while remaining:
            c = str(int(a) + int(b))
            
            if not remaining.startswith(c):
                return False
            
            remaining = remaining[len(c):]
            a, b = b, c
        
        return True