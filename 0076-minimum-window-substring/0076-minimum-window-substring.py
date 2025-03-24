class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_counts = Counter(t)
        required = len(t_counts)

        # left, right  pointer
        l, r = 0, 0
        formed = 0
        window_counts = defaultdict(int)

        ans = float("inf"), None, None

        while r < len(s):
            char = s[r]
            window_counts[char] += 1

            if char in t_counts and window_counts[char] == t_counts[char]:
                formed += 1

            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[s[l]] -= 1
                if s[l] in t_counts and window_counts[s[l]] < t_counts[s[l]]:
                    formed -= 1
                l += 1

            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]