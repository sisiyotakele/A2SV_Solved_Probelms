class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deq=deque()
        min_deq = deque()
        left = 0
        res=0
        for right in range(len(nums)):
            while max_deq and nums[right] > max_deq[-1]:
                max_deq.pop()
            max_deq.append(nums[right])

            while min_deq and nums[right] < min_deq[-1]:
                min_deq.pop()
            min_deq.append(nums[right])

            while max_deq[0] -min_deq[0] > limit:
                if nums[left] == max_deq[0]:
                    max_deq.popleft()
                if nums[left] == min_deq[0]:
                    min_deq.popleft()
                left += 1
            res = max(res,right - left + 1)
        return res

        