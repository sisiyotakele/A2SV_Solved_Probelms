class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frq ={}
        max_s = 0
        l = 0 
        max_frq=0
        for r in range(len(s)):
            frq[s[r]] = frq.get(s[r], 0) + 1
            max_frq = max(frq[s[r]] ,max_frq)
            while (r-l + 1 ) - max_frq > k:
                frq[s[l]] -= 1
                l += 1
            max_s = max(max_s,r-l+1)
        return max_s

