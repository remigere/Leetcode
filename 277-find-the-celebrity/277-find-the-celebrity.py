# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        for i in range(n):
            found = True
            for j in range(n):
                if j != i:
                    if not(knows(j, i)) or knows(i, j):
                        found = False
                        break
            if found:
                return i
        return -1
        """
        prec = 0
        for i in range(1, n):
            if knows(prec, i):
                prec = i
        found = True
        for j in range(n):
            if j != prec:
                if not(knows(j, prec)) or knows(prec, j):
                    found = False
                    return - 1
        return prec