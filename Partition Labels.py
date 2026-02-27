class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = {}
        for i,ch in enumerate(s):
            freq[ch] = i
        res = []
        st = 0
        l = 0
        for i, ch in enumerate(s):
            l = max(l,freq[ch])

            if l == i:
                res.append(l-st+1)
                st = i +1
        return res
