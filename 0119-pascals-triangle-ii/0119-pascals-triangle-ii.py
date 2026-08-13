class Solution:
    # def getRowCol(self, row, col):
    #     # Base case
    #     if row == 0 or col == 0 or col == row:
    #         return 1

    #     # Recursive case
    #     return self.getRowCol(row - 1, col - 1) + self.getRowCol(row - 1, col)

    # def getRow(self, rowIndex: int) -> List[int]:
    #     res = []
        
    #     for col in range(rowIndex + 1):
    #         res.append(self.getRowCol(rowIndex, col))

    #     return res
    def getRow(self, rowIndex):
        res= [1]
        for i in range(rowIndex):
            newRow=[1]
            for j in range(len(res)-1):
                newRow.append(res[j] +res[j+1])
            newRow.append(1)
            res = newRow
        return res