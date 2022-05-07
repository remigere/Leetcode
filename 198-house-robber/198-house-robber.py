class Solution:
    def rob(self, nums: List[int]) -> int:
        
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
                    
            