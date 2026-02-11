class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for i in s:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1
        sorted_s = dict(sorted(freq.items(), key=lambda item: item[1],reverse =True))   
        res=''
        for k in sorted_s:
            
            if sorted_s[k] > 1:
                cnt = sorted_s[k]
                res += (k*cnt)
            else:
                res += k
        return res

            
