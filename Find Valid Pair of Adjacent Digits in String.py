class Solution:
    def findValidPair(self, s: str) -> str:
        res=""
        s_c = Counter(s)
        n = len(s)
        for i in range(n-1):
            char1=s[i]
            char2 =s[i+1]

            if char1 != char2 :
                if int(char1) == s_c[char1] and int(char2) == s_c[char2]:
                    res = char1 + char2
                    break
                
        return res


                 

                
