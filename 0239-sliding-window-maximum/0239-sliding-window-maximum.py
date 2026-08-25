# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         res = []

#         for i in range(len(nums) - k + 1):
#             kthNum = nums[i:i + k]
#             res.append(max(kthNum))

#         return res
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for i in range(len(nums)):

            # Remove elements outside the window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # Add current index
            dq.append(i)

            # Start adding answers when window reaches size k
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res