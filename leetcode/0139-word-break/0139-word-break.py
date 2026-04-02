class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mapp = set(wordDict)
        memo = {}
        def backtrack(ind):
            if ind >= len(s):
                return True
            if ind in memo:
                return memo[ind]
            cur = ""
            for i in range(ind,len(s)):
                cur += s[i]
                if cur in mapp:
                    if backtrack(i + 1):
                        memo[ind] = True
                        return True
            memo[ind] = False
            return False
        return backtrack(0)