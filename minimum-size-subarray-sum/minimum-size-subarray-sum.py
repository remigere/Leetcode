class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        min_l = float("inf")
        i = 0
        sums = [None for _ in range(len(nums))]
        for i in range(len(nums)):
            l = 0
            s = 0
            while i + l < len(nums) and s < target:
                s += nums[i + l]
                l += 1
            #print(i, l, s)
            if s >= target:
                #print(s, l)
                min_l = min(min_l, l)
        return 0 if min_l == float("inf") else min_l
        """
        total = left = 0
        result = len(nums) + 1
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0