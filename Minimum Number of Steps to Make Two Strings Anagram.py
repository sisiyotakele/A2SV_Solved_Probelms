class Solution:
    def minSteps(self, s: str, t: str) -> int:
        t_c = Counter(t)
        s_c =  Counter(s)
        diff = t_c - s_c
        print(diff)
        return sum(diff.values())
