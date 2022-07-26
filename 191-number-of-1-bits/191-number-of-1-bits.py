class Solution:
    def hammingWeight(self, n: int) -> int:
        #return Counter(list(str(bin(n)[2:])))["1"]
        
        # count = 0
        # while n:
        #     if n % 2 == 1:
        #         count += 1
        #     n = n // 2
        # return count
        
        count = 0 
        while n:
            count += 1
            n &= n - 1
        return count