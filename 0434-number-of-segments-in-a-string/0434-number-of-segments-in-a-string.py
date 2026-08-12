class Solution:
    def countSegments(self, s: str) -> int:
        if s == "":
            return 0
        
        count = s.split()
        return len(count)