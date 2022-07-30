# class Solution:
#     def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
#         res = []
#         d1 = [Counter(word1) for word1 in words1]
#         c = defaultdict(int)
#         for word2 in words2:
#             c2 = Counter(word2)
#             for char in c2.keys():
#                 c[char] = max(c[char], c2[char])
#         for i, c1 in enumerate(d1):
#             flag = True
#             #print(c1, c)
#             for key, value in c.items():
#                 if key not in c1 or value > c1[key]:
#                     flag = False
#                     break
#             if flag:
#                 res.append(words1[i])
#         return res
    
class Solution(object):
    def wordSubsets(self, A, B):
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans