class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)

        ans = 0
        odd = False

        for cnt in freq.values():
            if cnt % 2 == 0:
                ans += cnt
            else:
                ans += cnt - 1
                odd = True

        return ans + odd