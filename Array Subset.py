from collections import Counter 
class Solution:
    def isSubset(self, a, b):
        # Your code here
        
        A = Counter(a)
        B = Counter(b)

        for x in B:
            if B[x] > A[x]:
                return False
        return True
    
    
    
    
