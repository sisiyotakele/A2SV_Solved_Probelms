class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        stack =[]
        mapping={}

        for num in nums2:
            while stack and num > stack[-1]:
                index=stack.pop()
                mapping[index] = num
            stack.append(num)
        return [mapping.get(n,-1) for n in nums1]