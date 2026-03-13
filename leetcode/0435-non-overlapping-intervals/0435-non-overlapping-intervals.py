class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1]) 
        print(intervals)
        count = 0
        last = -float('inf')
        for start, end in intervals:
            if start >= last:
                count += 1
                last = end
        return len(intervals) - count




            