class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * m for _ in range(n)]
        for i in reversed(range(n - 1)):
            for j in reversed(range(m - 1)):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]