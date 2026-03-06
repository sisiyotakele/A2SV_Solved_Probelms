class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a','e','i','o','u'}
        n = len(words)
        pref=[0] * (n+1)
        for i in range(n):
            word = words[i]

            if word[0] in vowels and word[-1] in vowels:
                is_good = 1
            else:
                is_good = 0

            pref[i+1] = pref[i] + is_good
        ans = []
        for l,r in queries:
            count=  pref[r+1] - pref[l]
            ans.append(count)
        return ans
        