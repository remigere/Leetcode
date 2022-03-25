class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        i = 0
        while i < len(nums):
            j = 0
            while i + j < len(nums) and nums[i + j] == 1:
                j += 1
            if j > m:
                m = j
            i += j + 1
        return m
                