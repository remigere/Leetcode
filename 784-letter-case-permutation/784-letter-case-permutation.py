class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def rec(s, cur_string):
            if len(s) == 0:
                ans.append(cur_string)
            else:
                if s[0].isnumeric():
                    rec(s[1:], cur_string + s[0])
                else:
                    rec(s[1:], cur_string + s[0].upper())
                    rec(s[1:], cur_string + s[0].lower())
        rec(s, "")
        return ans