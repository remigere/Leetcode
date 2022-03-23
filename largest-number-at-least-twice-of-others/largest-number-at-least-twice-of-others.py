class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        i = max(range(len(nums)), key=nums.__getitem__)
        for j in range(len(nums)):
            if i != j and nums[i] < 2 * nums[j]:
                return -1
        return i