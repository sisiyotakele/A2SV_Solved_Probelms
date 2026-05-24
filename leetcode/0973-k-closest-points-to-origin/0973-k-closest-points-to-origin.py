class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dis(p):
            return p[0]*p[0]+ p[1]*p[1]
        def quicksort(arr):
            if len(arr) <=1:
                return arr
            piv=dis(arr[len(arr)//2])
            
            l =[p for p in arr if dis(p) < piv]
            m =[p for p in arr if dis(p) == piv]
            r =[p for p in arr if dis(p) > piv]

            return quicksort(l) + m+ quicksort(r)
        sorted_p= quicksort(points)
        return sorted_p[:k]