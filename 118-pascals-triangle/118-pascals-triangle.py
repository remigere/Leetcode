class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        if numRows == 0:
            return ans
        ans.append([1])
        for row in range(1, numRows):
            ans.append([1] + [a + b for a, b in zip(ans[-1][:-1], ans[-1][1:])] + [1])
        return ans