class Solution:
    def subarraysDivByK(self, nums, k):
        total = 0
        count = 0
        
        freq = {0: 1}

        for num in nums:
            total += num

            remainder = total % k

            if remainder in freq:
                count += freq[remainder]

            if remainder in freq:
                freq[remainder] += 1
            else:
                freq[remainder] = 1

        return count