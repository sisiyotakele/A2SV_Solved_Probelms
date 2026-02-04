from collections import Counter 
class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        A=Counter(a)
        B=Counter(b)
        return A == B
