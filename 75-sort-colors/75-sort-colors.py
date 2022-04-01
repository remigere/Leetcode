class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        middle = left
        
        while middle <= right:
            if nums[middle] == 0:
                nums[middle], nums[left] = nums[left], nums[middle]
                left += 1
                middle += 1
            elif nums[middle] == 1:
                middle += 1
            else:
                    nums[middle], nums[right] = nums[right], nums[middle]
                    right -= 1
