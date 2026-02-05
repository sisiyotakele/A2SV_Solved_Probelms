class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        s = Counter(chars)
        res = []

        for w in words:
            wc = Counter(w)
            for c in wc:
                if wc[c] > s[c]:
                    break
            else:
                res.append(len(w))

        return sum(res)
