class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j = 0
        while j < len(strs[0]):
            flag = True
            for i in range(1, len(strs)):
                if j == len(strs[i]) or strs[i][j] != strs[0][j]:
                    flag = False
            if flag:
                j +=1
            else:
                break
        return strs[0][:j]