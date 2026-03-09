class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result= []
        for i in nums1:
            index=nums2.index(i)


            next_greater = -1
            for j in range(index +1 , len(nums2)):
                if nums2[j] > i:
                    next_greater = nums2[j]
                    break
            
            result.append(next_greater)
        return result

        
        # output=[]

        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             k = j+1
        #             if k == len(nums2):
        #                 output.append(-1)
        #             for n in range(k, len(nums2)):
        #                 if nums2[n] > nums2[j]:
        #                     output.append(nums2[n])
        #                     break
        #                 else:
        #                     output.append(-1)
        #                     break
        # return output  
                            
                            
        # #                 for x in range(j+1,len(nums2)):
        # #                 if nums2[x] > nums2[j]:
        # #                     output.append(nums2[j])
        # #                     break
        # #                 else:
        # #                     output.append(-1)
        # # return output