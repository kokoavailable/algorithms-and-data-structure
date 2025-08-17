class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)

        idx = lambda c: ord(c) - 97
        window = [0] * 26
        need = [0] * 26

        res = []

        # initialize need
        for c in p:
            need[idx(c)] += 1

        # initialize window
        for i in range(m):
            window[idx(s[i])] += 1

        # first check
        if window == need:
            res.append(0)

        for r in range(m, n):
            window[idx(s[r])] += 1
            window[idx(s[r-m])] -= 1
            if window == need:
                res.append(r-m+1)

        return res