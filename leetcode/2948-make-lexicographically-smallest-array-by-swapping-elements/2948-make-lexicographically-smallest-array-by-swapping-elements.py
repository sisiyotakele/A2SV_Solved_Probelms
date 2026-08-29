class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        sorted_pairs = sorted([(nums[i], i) for i in range(n)])
        
        ans = [0] * n
        i = 0
        while i < n:
            j = i + 1
            while j < n and sorted_pairs[j][0] - sorted_pairs[j-1][0] <= limit:
                j += 1
            
            indices = []
            for k in range(i, j):
                indices.append(sorted_pairs[k][1])
            
            indices.sort()
            
            for k in range(len(indices)):
                ans[indices[k]] = sorted_pairs[i + k][0]
            
            i = j
            
        return ans