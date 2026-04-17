class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        A = [nums1[i] - nums2[i] for i in range(len(nums1))]

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2
            left, left_count = merge_sort(arr[:mid])
            right, right_count = merge_sort(arr[mid:])

            count = 0
            i = 0

            for j in range(len(right)):
                while i < len(left) and left[i] <= right[j] + diff:
                    i += 1
                count += i

            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged, left_count + right_count + count

        _, result = merge_sort(A)
        return result