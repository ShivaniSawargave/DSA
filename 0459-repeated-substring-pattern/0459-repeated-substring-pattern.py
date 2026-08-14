class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for i in range(1, n):
            if n % i == 0:
                pattern = s[:i]

                if pattern * (n // i) == s:
                    return True

        return False