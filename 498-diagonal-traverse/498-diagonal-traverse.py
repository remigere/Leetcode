class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        N = len(mat)
        M = len(mat[0])
        for d in range(N + M - 1):
            cur = []
            r, c = 0 if d < M else d - M + 1, d if d < M else M - 1
            
            # Iterate until one of the indices goes out of scope
            # Take note of the index math to go down the diagonal
            while r < N and c > -1:
                cur.append(mat[r][c])
                r += 1
                c -= 1
            if d % 2 != 0:
                ans.extend(cur)
            else:
                ans.extend(reversed(cur))
        return ans