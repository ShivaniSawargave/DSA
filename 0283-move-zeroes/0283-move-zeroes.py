class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        nonZero = []
        zero = []

        for i in range(len(nums)):
            if nums[i] != 0:
                nonZero.append(nums[i])
            else:
                zero.append(nums[i])

        nums[:] = nonZero + zero