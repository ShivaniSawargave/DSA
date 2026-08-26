class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        binary = binary.zfill(32)

        binary = binary[::-1]

        number = int(binary, 2)

        return number