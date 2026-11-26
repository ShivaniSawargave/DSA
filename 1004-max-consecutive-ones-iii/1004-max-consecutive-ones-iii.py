class Solution:
    def longestOnes(self, nums, k):
        start = 0
        zeros = 0
        end = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                zeros += 1

            while zeros > k:
                if nums[start] == 0:
                    zeros -= 1

                start += 1

            end = max(end, i - start + 1)

        return end