class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sc=Counter(s)
        res=[]
        for i in order:
            if i in sc:
                res.extend([i] * sc[i])
        for k,v in sc.items():
            if k not in res:
                res.extend([k]* v)
        return "".join(res)
