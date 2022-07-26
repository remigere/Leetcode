class Solution:
    def hammingWeight(self, n: int) -> int:
        c = Counter(list(str(bin(n)[2:])))
        return c["1"]