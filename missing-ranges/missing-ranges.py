class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        cur = lower
        for num in nums + [upper + 1]:
            if num == cur + 1:
                ans.append(str(cur))
            elif num > cur + 1:
                ans.append(str(cur) + "->" + str(num - 1))
            cur = num + 1
        return ans