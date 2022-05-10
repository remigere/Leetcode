class Solution:
    def canPartition(self, nums: List[int]) -> bool:
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