class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        d = defaultdict(list)
        for word in strs:
            d[str(sorted(word))].append(word)
        return [anagrams for anagrams in d.values()]