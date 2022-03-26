class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        m = 0
        for right in range(len(s)):
            while s[right] in s[left : right]:
                left += 1
            m = max(m, right - left + 1)
        return m