class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        n = len(matrix)
        m = len(matrix[0])
        start_col = 0
        start_row = 0
        end_col = m - 1
        end_row = n - 1
        while end_col >= start_col and end_row >= start_row:
            if start_row == end_row:
                for j in range(start_col, end_col + 1):
                    ans.append(matrix[start_row][j])
            elif start_col == end_col:
                for i in range(start_row, end_row + 1):
                    ans.append(matrix[i][start_col])
            else:
                for j in range(start_col, end_col):
                    ans.append(matrix[start_row][j])
                for i in range(start_row, end_row):
                    ans.append(matrix[i][end_col])
                for j in reversed(range(start_col + 1, end_col + 1)):
                    ans.append(matrix[end_row][j])
                for i in reversed(range(start_row + 1, end_row + 1)):
                    ans.append(matrix[i][start_col])
            start_col += 1
            end_col -= 1
            start_row += 1
            end_row -= 1
        return ans