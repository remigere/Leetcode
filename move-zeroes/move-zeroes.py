class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = nums[0] != 0
        print(j)
        for i in range(1, len(nums)):
            if nums[i] != 0:
                if nums[i - 1] == 0:
                    nums[j], nums[i] = nums[i], nums[j]
                j += 1