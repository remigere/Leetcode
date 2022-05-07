class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        L = [k for k in range(1, 10)]
        output = []
        
        def backtracking(comb, start, k, n):
            if n == 0 and k == 0:
                output.append(list(comb))
                return
            elif n < 0 or k < 0:
                return
            else:
                for i in range(start + 1, len(L)):
                    backtracking(comb + [L[i]], i, k - 1, n - L[i])
                
        backtracking([], -1, k, n)
        return output
        