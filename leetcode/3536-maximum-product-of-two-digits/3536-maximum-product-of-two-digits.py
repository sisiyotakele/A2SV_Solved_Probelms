class Solution:
    def maxProduct(self, n: int) -> int:
        first = second = -1

        while n:
            digit = n % 10
            n //= 10

            if digit >= first:
                second = first
                first = digit
            elif digit > second:
                second = digit

        return first * second