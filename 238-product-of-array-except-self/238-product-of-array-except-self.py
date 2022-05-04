class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        num_zeros = len(nums)
        for num in nums:
            if num != 0:
                num_zeros -= 1
                prod *= num
        if num_zeros >= 2:
            return [0] * len(nums)
        elif num_zeros == 1:
            return [prod if num == 0 else 0 for num in nums]
        else:
            print(num_zeros)
            return [prod // num for num in nums]