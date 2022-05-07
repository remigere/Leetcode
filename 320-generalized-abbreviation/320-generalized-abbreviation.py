class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        output = []
        n = len(word)
        def backtracking(comb, start, cur):
            if start == n:
                if cur:
                    comb += str(cur)
                output.append(str(comb))
                return
            else:
                backtracking(comb, start + 1, cur + 1)
                if cur:
                    comb += str(cur)
                backtracking(comb + word[start], start + 1, 0)
            
        backtracking("", 0, 0)
        return output