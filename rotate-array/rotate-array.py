class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        def rotate1(nums):
            temp = nums[-1]
            for i in reversed(range(len(nums) - 1)):
                nums[i + 1] = nums[i]
            nums[0] = temp
        for _ in range(k):
            rotate1(nums)
        """
        moved = 0
        start = 0
        n = len(nums)
        while moved < n:
            cur = (start + k) % n
            temp = nums[start]
            #print(moved, cur, temp)
            while cur != start:
                #print("---", cur, nums[cur], temp)
                nums[cur], temp = temp, nums[cur]
                cur = (cur + k) % n
                moved += 1
            nums[start] = temp
            moved += 1
            #print("here", moved, cur, temp)
            #print(nums)
            start += 1
        