class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        target = Counter(str(n))

        power = 1
        while power <= 10**9:
            if Counter(str(power)) == target:
                return True
            power *= 2

        return False