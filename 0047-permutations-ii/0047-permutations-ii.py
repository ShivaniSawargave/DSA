class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = []
        path = []
        used = [False] * len(nums)

        def backtrack():

            if len(path) == len(nums):
                result.append(path.copy())
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                # Skip duplicate
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # Choose
                path.append(nums[i])
                used[i] = True

                # Explore
                backtrack()

                # Undo
                path.pop()
                used[i] = False

        backtrack()

        return result