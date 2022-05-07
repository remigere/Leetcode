class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(nums):
            n = len(nums)
            dp = [None for k in range(n + 1)]
            dp[-1] = 0
            dp[-2] = nums[-1]
            for i in range(n - 2, -1, -1):
                dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])
            return dp[0]
        if len(nums) == 1:
            return nums[0]
        return max(rob1(nums[1:]), rob1(nums[:-1]))