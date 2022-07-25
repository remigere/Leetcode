class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1
        
        def binary_search(start, end, target, pos):
            mid = (end + start) // 2
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    if pos == "last":
                        
                        if (mid == len(nums) - 1 or nums[mid] < nums[mid + 1]):
                            return mid
                        start = mid + 1
                        
                    elif pos == "first":
                        
                        if (mid == 0 or nums[mid] > nums[mid - 1]):
                            return mid
                        end = mid - 1
                        
                elif nums[mid] < target:
                    start = mid + 1
                    
                else:
                    end = mid - 1
            return -1
       
        return [binary_search(start, end, target, "first"), binary_search(start, end, target, "last")]
            
                
                