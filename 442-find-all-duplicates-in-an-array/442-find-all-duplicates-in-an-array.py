class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        s = {nums[0]}
        ans = []
        for num in nums[1:]:
            if num in s:
                ans.append(num)
            s.add(num)
        return ans
        """
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res