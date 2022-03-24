class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            return self.addBinary(b, a)
        b2 = "0" * (len(a) - len(b)) + b
        add = 0
        ans = ""
        print(b2)
        for i, val in enumerate(reversed(b2)):
            ans += str((int(a[-i - 1]) + int(val) + add) % 2)
            add = (int(a[-i - 1]) + int(val) + add) // 2
        if add == 1:
            ans += str(add)
        return ans[::-1]