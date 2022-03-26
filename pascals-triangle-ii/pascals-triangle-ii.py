class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        if rowIndex == 0:
            return row
        for i in range(rowIndex):
            row = [1] + [a + b for a, b in zip(row[1:], row[:-1])] + [1]
        return row