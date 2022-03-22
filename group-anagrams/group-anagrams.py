class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        ans = [(Counter(strs[0]), [strs[0]])]
        for i in range(1, len(strs)):
            c = Counter(strs[i])
            added = False
            for j in range(len(ans)):
                if c == ans[j][0]:
                    ans[j][1].append(strs[i])
                    added = True
                    break
            if not added:
                ans.append((c, [strs[i]]))
        #print(ans)
        return [ana for _, ana in ans]
            
        """
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()