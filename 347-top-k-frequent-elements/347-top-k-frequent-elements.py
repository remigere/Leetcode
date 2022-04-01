class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = Counter(nums)
        return sorted(d.keys(), key = lambda x: d[x], reverse = True)[:k]
        """
        n = len(nums)
        count = Counter(nums)
        unique = list(count.keys())
        
        def partition(left, right, pivot_index):
            pivot_frequency = count[unique[pivot_index]]
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[i], unique[store_index] = unique[store_index], unique[i]
                    store_index += 1
            unique[store_index], unique[right] = unique[right], unique[store_index]
            return store_index
        
        def quickselect(left, right, k_smallest):
            if left == right:
                return
            
            pivot_index = random.randint(left, right)
            store_index = partition(left, right, pivot_index)
            if store_index == k_smallest:
                return
            elif store_index < k_smallest:
                quickselect(store_index + 1, right, k_smallest)
            else:
                quickselect(left, store_index - 1, k_smallest)
        
        quickselect(0, n, n - k)
        
        return unique[n - k:]
        """