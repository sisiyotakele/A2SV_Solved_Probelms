class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = [0] * len(A)
        seen = [0] * (len(A) + 1)
        for i in range(len(A)):
            seen[0] += seen[A[i]]
            seen[A[i]] = 1

            seen[0] += seen[B[i]]
            seen[B[i]] = 1

            res[i] = seen[0]
        return res


        
