class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if not strs:
        #     return [[""]]
        # d = defaultdict(list)
        # for word in strs:
        #     d[str(sorted(word))].append(word)
        # return d.values()
    

        d = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord("a")] += 1
            d[tuple(key)].append(word)
        return d.values()