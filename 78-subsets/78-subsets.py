class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            new = []
            for cur in output:
                new.append(cur + [num])
            output.extend(new)
        
        return output