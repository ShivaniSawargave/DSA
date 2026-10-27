class Solution:
    def createGrid(self, m, n):
        result = []                      # will hold our rows

        for i in range(m):               # go through each row
            if i == m - 1:
                row = "." * n            # last row: all open
            else:
                row = "." + "#" * (n - 1)  # other rows: first cell open, rest blocked
            result.append(row)

        return result