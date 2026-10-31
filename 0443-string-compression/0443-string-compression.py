class Solution:
    def compress(self, chars: list[str]) -> int:

        i = 0
        result = []

        while i < len(chars):

            count = 1

            while i + 1 < len(chars) and chars[i] == chars[i+1]:
                count += 1
                i += 1

            result.append(chars[i])

            if count > 1:
                result.extend(list(str(count)))

            i += 1

        chars[:len(result)] = result

        return len(result)