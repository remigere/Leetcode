class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []
        def backtracking(n, comb, k):
            if n == 0 and k == 0:
                output.append(str(comb))
                return
            elif n < 0 or k < 0:
                return
            else:
                backtracking(n - 1, comb + "(", k + 1)
                backtracking(n - 1, comb + ")", k - 1)
                
        backtracking(2 * n, "", 0)
        return output