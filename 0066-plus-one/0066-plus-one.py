class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0

        for digit in digits:
            num = num * 10 + digit
        num = num + 1 
        arr = []
        while num > 0:
            arr.append(num % 10)
            num //= 10
        arr.reverse()
        return arr