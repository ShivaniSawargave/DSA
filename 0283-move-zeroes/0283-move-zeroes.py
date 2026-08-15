class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        arr = []
        zero = []

        for i in range(len(nums)):
            if nums[i] == 0:
                zero.append(nums[i])
            else:
                arr.append(nums[i])

        nums[:] = arr + zero