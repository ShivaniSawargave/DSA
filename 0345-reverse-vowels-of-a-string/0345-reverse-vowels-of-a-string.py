class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        si = 0
        ei =len(s)-1
        arr = list(s)
        while si < ei:
            if arr[si]  not in vowels:
                si += 1
            elif arr[ei]  not in vowels:
                ei -=1
            else:
                arr[si], arr[ei] = arr[ei], arr[si]
                si += 1
                ei -= 1
        res = "".join(arr)
        return res  