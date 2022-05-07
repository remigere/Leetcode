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
        n = len(nums)
        
        memo = {}
        def dfs(start, remain):
            if (start, remain) not in memo:
                if start == n:
                    if remain == 0:
                        memo[(start, remain)] = 1
                    else:
                        memo[(start, remain)] = 0
                else:
                    sub = dfs(start + 1, remain - nums[start])
                    add = dfs(start + 1, remain + nums[start])
                    memo[(start, remain)] = sub + add
            return memo[(start, remain)]
        return dfs(0, target)