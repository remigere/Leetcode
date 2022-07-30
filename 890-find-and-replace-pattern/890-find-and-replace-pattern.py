# class Solution(object):
#     def findAndReplacePattern(self, words, pattern):
#         def match(word):
#             m1, m2 = {}, {}
#             for w, p in zip(word, pattern):
#                 if w not in m1: m1[w] = p
#                 if p not in m2: m2[p] = w
#                 if (m1[w], m2[p]) != (p, w):
#                     return False
#             return True

#         return filter(match, words)

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            P = {}
            for x, y in zip(pattern, word):
                if P.setdefault(x, y) != y:
                    return False
            return len(set(P.values())) == len(P.values())

        return filter(match, words)