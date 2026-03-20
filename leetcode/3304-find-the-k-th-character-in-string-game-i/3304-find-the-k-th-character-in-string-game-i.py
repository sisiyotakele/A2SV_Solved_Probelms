class Solution:
    def kthCharacter(self, k: int) -> str:
        shift = 0
    
        while k > 1:
            half = 1
            while half * 2 < k:
                half *= 2
            
            k -= half
            shift += 1
        
        return chr(ord('a') + shift)