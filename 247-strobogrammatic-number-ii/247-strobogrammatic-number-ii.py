class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res = []        
        
        def rec(n, cur, non_zero):
            nonlocal res
            
            def mirror(x):
                if x == "1":
                    return "1"
                elif x == "6":
                    return "9"
                elif x == "9":
                    return "6"
                elif x == "8":
                    return "8"
                elif x == "0":
                    return "0"
                
            if n == 1:
                res.extend([cur + mid + "".join(mirror(x) for x in cur[::-1]) for mid in ("0", "1", "8")])
            elif n == 0:
                res.append(cur + "".join(mirror(x) for x in cur[::-1]))
            else:
                rec(n - 2, cur + "1", True)
                rec(n - 2, cur + "6", True)
                rec(n - 2, cur + "9", True)
                rec(n - 2, cur + "8", True)
                if non_zero:
                    rec(n - 2, cur + "0", True)
        
        rec(n, "", False)
        return res
                