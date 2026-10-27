
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0

        for i in range(n):
            position = i + 1

            if n % position == 0:
                total += nums[i] * nums[i]

        return total
