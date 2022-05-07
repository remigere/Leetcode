class Solution:
    def rob(self, nums: List[int]) -> int:
        
        """
        n = len(nums)
        output = 0
        
        @lru_cache(None)
        def dfs(start, prev, cur):
            nonlocal output
            if start == n:
                output = max(output, cur)
                return
            else:
                dfs(start + 1, False, cur)
                if not prev:
                    dfs(start + 1, True, cur + nums[start])
        
        dfs(0, False, 0)
        return output
        """
        
        # bottom up
        n = len(nums)
        dp = [[0 for k in range(2)] for i in range(n + 1)]
        dp[0][1] = -float("inf")
        for i in range(n):
            dp[i + 1][0] = max(dp[i][1], dp[i][0])
            dp[i + 1][1] = dp[i][0] + nums[i]
        return max(dp[-1])