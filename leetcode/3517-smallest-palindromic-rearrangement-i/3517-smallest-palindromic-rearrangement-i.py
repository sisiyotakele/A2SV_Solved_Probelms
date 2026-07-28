class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        half_len = n // 2
        left_half = sorted(list(s[:half_len]))
        
        mid = s[half_len] if n % 2 != 0 else ""
        
        left_str = "".join(left_half)
        return left_str + mid + left_str[::-1]