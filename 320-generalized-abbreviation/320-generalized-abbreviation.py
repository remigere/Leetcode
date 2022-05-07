class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        output = []
        n = len(word)
        def backtracking(comb, start, cur):
            if start == n:
                if cur:
                    output.append(str(comb) + str(cur))
                else:
                    output.append(str(comb))
                return
            else:
                if start == 0:
                    backtracking(comb, start + 1, 1)
                    backtracking(comb + word[start], start + 1, 0)
                else:
                    if cur:
                        backtracking(comb + str(cur) + word[start], start + 1, 0)
                        backtracking(comb, start + 1, cur + 1)
                    else:
                        backtracking(comb + word[start], start + 1, 0)
                        backtracking(comb, start + 1, 1)
            
        backtracking("", 0, 0)
        return output