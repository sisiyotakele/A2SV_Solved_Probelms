class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()

        arr = sorted((num, i) for i, num in enumerate(nums2))

        n = len(nums1)
        ans = [0] * n

        left, right = 0, n - 1

        for num, idx in reversed(arr):
            if nums1[right] > num:
                ans[idx] = nums1[right]
                right -= 1
            else:
                ans[idx] = nums1[left]
                left += 1

        return ans