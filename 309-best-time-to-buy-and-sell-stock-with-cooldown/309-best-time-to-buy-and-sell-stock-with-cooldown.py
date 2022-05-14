class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 3 for _ in range(len(prices) + 1)]
        dp[0][1] = - float("inf")
        dp[0][2] = - float("inf")
        for k in range(1, len(dp)):
            dp[k][0] = max(dp[k - 1][0], dp[k - 1][2])
            dp[k][1] = max(dp[k - 1][0] - prices[k - 1], dp[k - 1][1])
            dp[k][2] = dp[k - 1][1] + prices[k - 1]
        print(dp)
        return max(dp[-1])