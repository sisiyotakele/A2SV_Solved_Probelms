class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        pref_xor = [0] * (n+1) 
        for i in range(n):
            pref_xor[i+1] = pref_xor[i] ^ arr[i]
        
        ans = []
        for l,r in queries:
            L = l + 1
            R = r + 1
            res = pref_xor[R] ^ pref_xor[L-1]
            ans.append(res)
        return ans