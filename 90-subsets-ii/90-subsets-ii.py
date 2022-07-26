class Solution:
#     def subsetsWithDup(self, nums):
#         ret = []
#         self.dfs(sorted(nums), [], ret)
#         return ret
    
#     def dfs(self, nums, path, ret):
#         ret.append(path)
#         for i in range(len(nums)):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             self.dfs(nums[i+1:], path+[nums[i]], ret)
#     
    def subsetsWithDup(self, nums):
        nums.sort()
        subsets = []
        n = len(nums)
        m = 2 ** n
        seen = set()
        for i in range(m):
            cur = []
            hashcode = ""
            for j in range(n):
                mask = 1 << j
                isSet = mask & i
                if isSet:
                    cur.append(nums[j])
                    hashcode += str(nums[j]) + ","
            if hashcode not in seen:
                seen.add(hashcode)
                subsets.append(cur)
        return subsets
        