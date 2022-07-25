class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1
        
        def binary_search(start, end, target):
            mid = (end + start) // 2
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target and (mid == len(nums) - 1 or nums[mid] < nums[mid + 1]):
                    return mid
                elif nums[mid] <= target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
        
        def binary_search2(start, end, target):
            mid = (end + start) // 2
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target and (mid == 0 or nums[mid] > nums[mid - 1]):
                    return mid
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
        
        return [binary_search2(start, end, target), binary_search(start, end, target)]
        print(binary_search(start, end, target))
        return
            
                
                