class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        # 2n - 1 center
        
        print("here")
        
        def pal(i, j):
            print(i, j)
            while 0 <= i and j <= len(s) - 1:
                if s[i] == s[j]:
                    i = i - 1
                    j = j + 1
                    self.count += 1
                else:
                    break
            return
        
        for i in range(len(s)):
            pal(i, i)
            if i < len(s) - 1:
                pal(i, i + 1)
        
        return self.count