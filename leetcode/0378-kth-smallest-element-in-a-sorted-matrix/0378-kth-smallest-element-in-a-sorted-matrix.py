class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        large = []
        for m in matrix:
            large.extend(m)
        heap = []
        for i in large:
            heapq.heappush(heap , -i)
            if len(heap) > k:
                -heapq.heappop(heap)
        return -heap[0]

