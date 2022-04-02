class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find k rotation in O(logn)
        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0
            
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
        
        def search_target(left, right):
            print(left, right)
            if left > right:
                return -1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return search_target(left, mid - 1)
            else:
                return search_target(mid + 1, right)
        

        n = len(nums)

        if n == 1:
            return 0 if nums[0] == target else -1

        rotate_index = find_rotate_index(0, n - 1)

        # if target is the smallest element
        if nums[rotate_index] == target:
            return rotate_index
        # if array is not rotated, search in the entire array
        if rotate_index == 0:
            return search_target(0, n - 1)
        if target < nums[0]:
            # search on the right side
            return search_target(rotate_index, n - 1)
        # search on the left side
        return search_target(0, rotate_index)