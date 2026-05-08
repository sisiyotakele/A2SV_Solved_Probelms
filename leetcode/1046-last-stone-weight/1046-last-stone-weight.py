class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for x in stones:
            heapq.heappush(max_heap , -x)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap) 
            second = -heapq.heappop(max_heap) 
            if first != second:
                new_ele = first - second
                heapq.heappush(max_heap , -new_ele)
        return -max_heap[0] if max_heap else 0 
        #     c += 1
        #     max_val = -heapq.heappop(max_heap)
        #     if c != 2:
        #         prev = max_val
        #         continue
        #     else:
        #         c = 0
                
        #     if prev == max_val:
        #         heapq.heappop(stones)
        #         heapq.heappop(stones)
        #     if prev != max_val: 
        #         heapq.heappop(stones)
        #         heapq.heappop(stones)
        #         max_heap.push(stones, abs(max_val - prev))

        # return max_heap[0]


