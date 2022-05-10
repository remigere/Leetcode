class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        
        n = len(nums)
        
        s = sum(nums)
        if s % 2 == 1:
            return False
        
        @lru_cache(None)
        def dfs(index, remain):
            if remain < 0 or (remain > 0 and index == n):
                return False
            elif remain == 0:
                return True
            else:
                return dfs(index + 1, remain) or dfs(index + 1, remain - nums[index])
            
        return dfs(0, s // 2)
        """
        n = len(nums)
        
        s = sum(nums)
        if s % 2 == 1:
            return False
        
        dp = [[False] * (s // 2 + 1 + 1) for _ in range(n + 1)]
        dp[0][0] = True
        
        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(s // 2 + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        return dp[n][s // 2]
            