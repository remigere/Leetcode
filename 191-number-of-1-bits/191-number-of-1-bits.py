class Solution:
    def hammingWeight(self, n: int) -> int:
        return Counter(list(str(bin(n)[2:])))["1"]