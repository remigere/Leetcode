class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # binary-search
        def binary_search(left, right):
            """
            #print(left, right)
            if left == right:
                return left
            mid = (left + right) // 2
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    return binary_search(mid + 1, right)
            elif mid == len(nums) - 1:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    return binary_search(left, mid - 1)
            else:
                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    return mid
                elif nums[mid] >= nums[mid - 1]:
                    return binary_search(mid + 1, right)
                else:
                    return binary_search(left, mid - 1)
            """
            if left == right:
                return left
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return binary_search(left, mid )
            else:
                return binary_search(mid + 1, right)
            
        return binary_search(0, len(nums) - 1)