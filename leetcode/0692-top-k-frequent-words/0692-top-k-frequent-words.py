class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        for w, freq in count.items():
            heapq.heappush(heap, (-freq, w))

        return [heapq.heappop(heap)[1] for _ in range(k)]