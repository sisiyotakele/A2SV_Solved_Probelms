class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mapp = set(wordDict)
        @cache
        def backtrack(ind):
            if ind >= len(s):
                return True
            cur = ""
            for i in range(ind,len(s)):
                cur += s[i]
                if cur in mapp:
                    if backtrack(i + 1):
                        return True
            return False
        return backtrack(0)