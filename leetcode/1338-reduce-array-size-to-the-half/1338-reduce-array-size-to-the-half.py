class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)

        counts = sorted(freq.values(), reverse=True)

        removed = 0
        ans = 0
        target = len(arr) // 2

        for c in counts:
            removed += c
            ans += 1
            if removed >= target:
                return ans