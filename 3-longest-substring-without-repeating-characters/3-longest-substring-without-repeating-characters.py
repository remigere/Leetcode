class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i = 1
        while i < len(s):
            for j in range(len(s) - i):
                flag = False
                cur = s[j : j + i + 1]
                if len(Counter(cur)) == i + 1:
                    flag = True
                    break
            if flag:
                i += 1
            else:
                break
        return i