class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        if s[0] == '0':
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            one = s[i - 1]
            two = s[i - 2:i]

            if '1' <= one <= '9':
                dp[i] += dp[i - 1]

            if '10' <= two <= '26':
                dp[i] += dp[i - 2]

        return dp[n]