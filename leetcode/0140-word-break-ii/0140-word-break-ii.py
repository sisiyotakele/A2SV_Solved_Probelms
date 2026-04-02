class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        mapp = set(wordDict)
        res = []
        def backtrack(ind, curr):
            if ind >= len(s):
                res.append(" ".join(curr))
                return

            temp = ""
            for i in range(ind , len(s)):
                temp += s[i]
                if temp in mapp:
                    backtrack(i + 1, curr + [temp])

            return
        backtrack(0,[])
        return res


