class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        coins.sort(reverse = True)
        n = len(coins)
        @lru_cache(None)
        def dfs(start, remain, count):
            if start == n and remain == 0:
                return count
            elif start == n and remain != 0:
                return float("inf")
            else:
                res = float("inf")
                for i in range(start, len(coins)):
                    res = min(res, dfs(i, amount - coins[i], count + 1))
                return res
        dfs(0, amount, 0)
        """
        
        @lru_cache(None)
        def dp(amount):
            if amount == 0:
                return 0
            
            ans = math.inf
            for coin in coins:
                if amount >= coin:
                    ans = min(ans, dp(amount - coin) + 1)
            return ans
        
        ans = dp(amount)
        return ans if ans != math.inf else -1
        