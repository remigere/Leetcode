class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def recursion(nums, cur_list):
            if len(nums) == 0:
                ans.append(cur_list)
            else:
                recursion(nums[1:], cur_list)
                recursion(nums[1:], cur_list + [nums[0]])
        recursion(nums, [])
        return ans