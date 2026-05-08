class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        heap = []
        for i in range(len(nums1)):
            heapq.heappush(heap ,(nums1[i] + nums2[0],i,0))
        while k > 0:
            s, i, j = heapq.heappop(heap)
            res.append([nums1[i],nums2[j]])
            k -= 1
            
            if j + 1 < len(nums2):
                heapq.heappush(heap , (nums1[i] + nums2[j+ 1],i,j+1))
           
        return res




        # res = []
        # smallestX = nums1[0]
        # smallestY = nums2[0]
        # heap1 = []
        # heap2 = []
        # for num in nums1:
        #         heapq.heappush(heap1,num) 
        # for n in nums2:
        #     heapq.heappush(heap2, n)
            
        # while k > 0:
        #     x = heapq.heappop(heap1)
        #     if x <= smallestX:
        #         smallestX = x
        #     y = heapq.heappop(heap2)
        #     if y <= smallestY:
        #         smallestY = y

        #     res.append([smallestX,smallestY])
        #     k -= 1
        # return res

            

