class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dictionary ={}
        n =len(s)
        i = 0 
        j = 0
        res=''
        while i < n:
            dictionary[indices[j]] = s[i] 
            i += 1
            j += 1
        res_sorted = sorted(dictionary.items())
        res = [value for key, value in res_sorted]

        return "".join(res)
            
        
