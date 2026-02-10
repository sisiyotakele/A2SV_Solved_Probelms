class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_table = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        i = 0
        n = len(s)
        res =[]
        while i < n :
            if i == n - 1 or  symbol_table[s[i]]>= symbol_table[s[i + 1]]:
                res.append(symbol_table[s[i]])
                i += 1
            else:
                res.append(symbol_table[s[i+1]]-symbol_table[s[i]])
                i += 2             
        return sum(res)


