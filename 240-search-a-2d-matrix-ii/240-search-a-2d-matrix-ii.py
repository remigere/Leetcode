class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        i, j = n - 1, 0
        while 0 <= i < n and 0 <= j < m:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i = i - 1
            else:
                j = j + 1
        return False