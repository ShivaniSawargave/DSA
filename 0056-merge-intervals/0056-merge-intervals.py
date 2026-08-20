class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        small = intervals[0][0]
        big = intervals[0][1]
        for i in range(1, len(intervals)):
            next_small = intervals[i][0]
            next_big = intervals[i][1]

            if next_small <= big:
                big = max(big, next_big)
            else:
                res.append([small, big])
                small = next_small
                big = next_big

        res.append([small, big])

        return res
