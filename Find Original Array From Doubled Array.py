class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed ) % 2==1:
            return []
        changed.sort()
        counter = Counter(changed)
        original = []
        print(counter)
        for x in changed:
            if counter[x] == 0:
                continue
            if counter[x*2] ==0:
                return []
            
            original.append(x)
            counter[x] -= 1
            counter[x*2] -= 1
        return original
