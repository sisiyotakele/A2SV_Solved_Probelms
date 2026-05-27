class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0

        for ch in "abcdefghijklmnopqrstuvwxyz":
            lower_last = word.rfind(ch)
            upper_first = word.find(ch.upper())

            if upper_first != -1 and lower_last != -1:
                if lower_last < upper_first:
                    count += 1

        return count