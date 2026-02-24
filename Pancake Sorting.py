class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for i in range(n , 1 , - 1):
            max_idx = arr.index(i)
            if max_idx != i - 1:
                if max_idx != 0:
                    arr [:max_idx+1] = reversed(arr[:max_idx+1])
                    res.append(max_idx + 1)

                arr[:i] = reversed(arr[:i])
                res.append(i)

        return res
