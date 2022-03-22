class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        n = len(matrix)
        m = len(matrix[0])
        rows, cols = [], []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        for i in rows:
            for j in range(m):
                matrix[i][j] = 0
        for j in cols:
            for i in range(n):
                matrix[i][j] = 0
        """
        
        n = len(matrix)
        m = len(matrix[0])
        flag = False
        
        for i in range(n):
            
            if matrix[i][0] == 0:
                flag = True
                
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        if matrix[0][0] == 0:
            for j in range(1, m):
                matrix[0][j] = 0
        
        if flag is True:
            for i in range(n):
                matrix[i][0] = 0
            