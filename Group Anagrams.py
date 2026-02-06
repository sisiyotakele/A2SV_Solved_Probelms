
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_d=defaultdict(list)
        for s in strs:
            k = "".join(sorted(s))
            print(k)
            s_d[k].append(s)
            print(s_d)
        return list(s_d.values())
