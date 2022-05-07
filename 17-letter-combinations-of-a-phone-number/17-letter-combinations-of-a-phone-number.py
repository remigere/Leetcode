class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        output = []
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if n == 0:
            return []
        def backtracking(comb, start):
            if start == n:
                output.append(str(comb))
                return
            else:
                for s in d[digits[start]]:
                    backtracking(comb + s, start + 1)
        
        backtracking("", 0)
        return output