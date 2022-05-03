class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(start, end):
            #print(start, end)
            if start > end:
                return -1
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary(start, mid - 1)
            else:
                print("here")
                return binary(mid + 1, end)
        return binary(0, len(nums) - 1)