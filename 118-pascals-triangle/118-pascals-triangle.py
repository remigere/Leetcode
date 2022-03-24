class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for row in range(numRows):
            if row == 0:
                ans.append([1])
            
            else:
                cur = [1] + [a + b for a, b in zip(ans[-1][:-1], ans[-1][1:])] + [1]
                ans.append(cur)
        return ans