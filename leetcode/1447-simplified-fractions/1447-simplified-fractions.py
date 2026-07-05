class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []

        for denm in range(2, n + 1):
            for numerator in range(1, denm):
                if gcd(numerator, denm) == 1:
                    ans.append(f"{numerator}/{denm}")

        return ans