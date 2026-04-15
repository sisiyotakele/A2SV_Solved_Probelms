class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        def canPlaceBalls(positions,m,X):
            count = 1
            last = positions[0]
            for i in range(1 ,n):
                if positions[i] - last >= X:
                    count += 1
                    last = positions[i]
                if count == m:
                    return True
            return False
        position.sort()
        ans = 0
        l = 1 
        h = position[-1] - position[0]
        while l <= h:
            mid = (l+h) // 2
            if canPlaceBalls(position ,m, mid):
                ans = mid 
                l = mid + 1
            else:
                h = mid - 1
        return ans
        