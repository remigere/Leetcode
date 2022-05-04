class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
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
        """
        """
        answer = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    answer[j] *= nums[i]
        return 
        answer = [1] * len(nums)
        """
        answer = [1] * len(nums)
        left_prod = 1
        right_prod = 1
        for i, j in zip(range(len(nums) - 1), reversed(range(1, len(nums)))):
            left_prod *= nums[i]
            right_prod *= nums[j]
            #print(left_prod, right_prod)
            answer[i + 1] *= left_prod
            answer[j - 1] *= right_prod
        return answer