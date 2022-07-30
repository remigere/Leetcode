class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        d1 = [Counter(word1) for word1 in words1]
        c = defaultdict(int)
        for word2 in words2:
            c2 = Counter(word2)
            for char in c2.keys():
                c[char] = max(c[char], c2[char])
        for i, c1 in enumerate(d1):
            flag = True
            #print(c1, c)
            for key, value in c.items():
                if key not in c1 or value > c1[key]:
                    flag = False
                    break
            if flag:
                res.append(words1[i])
        return res
    