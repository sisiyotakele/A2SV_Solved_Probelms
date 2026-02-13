class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        word = s.split(" ")
        pat = {}
        
        if len(pattern) != len(word):
            return False
        
        for i in range(len(pattern)):
            
            if pattern[i] not in pat:
                if word[i] in pat.values():
                    return False
                pat[pattern[i]] = word[i]
           
            elif pat[pattern[i]] != word[i]:
                return False
        
        return True
