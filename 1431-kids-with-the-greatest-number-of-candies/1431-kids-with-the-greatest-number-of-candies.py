class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        great = max(candies)
        res = []
        for i in range(len(candies)):
            kid = candies[i] + extraCandies
            if kid >= great:
                res.append(True)
            else :
                res.append(False)
        return res
            
        