class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(start, prod):
            if start == len(nums):
                return prod
            else:
                return max(prod, dfs(start + 1, prod * nums[start]), dfs(start + 1, nums[start]))
            
        return dfs(1, nums[0])
        
            