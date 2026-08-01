class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        ans = 10
        cur = 9
        available = 9

        for _ in range(2, n + 1):
            cur *= available
            ans += cur
            available -= 1

        return ans