class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        n = len(nums)
        output = 0
        
        def backtracking(start, remain):
            nonlocal output 
            if remain == 0 and start == n:
                output += 1
                return
            elif remain != 0 and start == n:
                return
            else:
                backtracking(start + 1, remain - nums[start])
                backtracking(start + 1, remain + nums[start])
        
        backtracking(0, target)
        return output
        """
        total = sum(nums)
        dp = [[0] * (2 * total + 1) for _ in range(len(nums) + 1)]
        # start at 0 (total is the middle element)
        dp[0][total] = 1
        for i, num in enumerate(nums):
            for s in range(2 * total + 1):
                #print(i + 1, s + num, s - num)
                #print("len", len(dp), len(dp[0]))
                if dp[i][s] > 0:
                    dp[i + 1][s + num] += dp[i][s]
                    dp[i + 1][s - num] += dp[i][s]
        if abs(target) > total:
            return 0
        else:
            return dp[-1][total + target]