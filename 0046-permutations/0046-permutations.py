class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path):
            # If permutation is complete
            if len(path) == len(nums):
                result.append(path.copy())
                return

            # Try every number
            for num in nums:
                if num not in path:
                    path.append(num)

                    backtrack(path)

                    path.pop()

        backtrack([])

        return result