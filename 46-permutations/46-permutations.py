class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(nums, cur):
            if len(nums) == 0:
                ans.append(cur)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], cur + [nums[i]])
        dfs(nums, [])
        return ans