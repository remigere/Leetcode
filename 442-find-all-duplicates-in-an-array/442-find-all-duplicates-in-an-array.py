class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = {nums[0]}
        ans = []
        for num in nums[1:]:
            if num in s:
                ans.append(num)
            s.add(num)
        return ans