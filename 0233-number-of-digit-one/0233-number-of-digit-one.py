class Solution:
    def countDigitOne(self, n):
        # count = 0

        # for i in range(1, n + 1):
        #     num = i

        #     while num > 0:
        #         if num % 10 == 1:
        #             count += 1
        #         num //= 10

        # return count
        count = 0
        factor = 1

        while factor <= n:
            higher = n // (factor * 10)
            current = (n // factor) % 10
            lower = n % factor

            if current == 0:
                count += higher * factor
            elif current == 1:
                count += higher * factor + lower + 1
            else:
                count += (higher + 1) * factor

            factor *= 10

        return count