class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        visited = {}
        max_len = 0

        for i in range(len(s)):
            if s[i] in visited:
                start = max(start, visited[s[i]] + 1)
            max_len = max(max_len, i - start + 1)
            visited[s[i]] = i

        return max_len