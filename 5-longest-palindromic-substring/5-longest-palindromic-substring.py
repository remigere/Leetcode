class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        # naive
        
        def palindrome(s):
            flag = True
            for i in range(len(s) // 2):
                if s[i] != s[-i - 1]:
                    flag = False
            return flag
            
        m, pal = 0, None
        for i in range(len(s)):
            for j in range(i, len(s)):
                if palindrome(s[i : j + 1]):
                    if j - i + 1 > m:
                        m = j - i + 1
                        pal = s[i : j + 1]
        return pal
        """
        n, ans = len(s), ""
        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i, j = i - 1, j + 1
            return s[i + 1:j]
        
        for k in range(n):
            ans = max(helper(k, k), helper(k, k + 1), ans, key=len)
        return ans