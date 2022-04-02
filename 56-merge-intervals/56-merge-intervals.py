class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #intervals.sort(key = lambda x: (x[0], x[1]))
        
        def pivot(left, right, pivot_index):
            pivot_value = intervals[pivot_index][0]
            intervals[pivot_index], intervals[right] = intervals[right], intervals[pivot_index]
            store_index = left
            for i in range(left, right):
                if intervals[i][0] <= pivot_value:
                    intervals[i], intervals[store_index] = intervals[store_index], intervals[i]
                    store_index += 1
            intervals[store_index], intervals[right] = intervals[right], intervals[store_index]
            return store_index
            
        def quicksort(left, right):
            if left >= right:
                return
            
            
            pivot_index = random.randint(left, right)
            sorted_index = pivot(left, right, pivot_index)
            if sorted_index > 0:
                quicksort(left, sorted_index - 1)
            if sorted_index < len(intervals) - 1:
                quicksort(sorted_index + 1, right)
        
        quicksort(0, len(intervals) - 1)
        
        
        
        print(intervals)
        if len(intervals) <= 1:
            return intervals
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                if intervals[i][1] > merged[-1][1]:
                    merged[-1][1] = intervals[i][1]
            else:
                merged.append(intervals[i])
        return merged