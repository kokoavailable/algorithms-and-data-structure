class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l, r):
            cnt = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            return cnt

        total = 0
        for i in range(len(s)):
            total += expand(i, i)
            total += expand(i, i+1)
        return total