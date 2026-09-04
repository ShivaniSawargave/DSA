class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        # If k digits are still left, remove from the end
        if k > 0:
            stack = stack[:-k]

        # Remove leading zeros
        result = ''.join(stack).lstrip('0')

        return result if result else '0'