class Solution:
    def partition(self, s: str) -> List[List[str]]:

        """
        def ispalindrome(s):
            for i in range(len(s) // 2):
                if s[i] != s[- i - 1]:
                    return False
            return True
        
        output = []  
        n = len(s)
        
        def backtracking(comb, cur, start, l):
            if start == n:
                if l == n:
                    output.append(list(comb))
                return
            else:
                new = cur + s[start]
                if ispalindrome(new):
                    backtracking(comb + [new], "", start + 1, l + len(new))
                backtracking(comb, new, start + 1, l)
        
        backtracking([], "", 0, 0)
        return output
    
        """
        res = []
        self.dfs(s, [], res)
        return res
    
    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)

    def isPal(self, s):
        return s == s[::-1]