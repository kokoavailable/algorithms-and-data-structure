class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:
            return s
        
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_length = 1
        
        for i in range(n):
            dp[i][i] = True
            
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i+1] = True
                start = i
                max_length = 2
                
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_length:
                        start = i
                        max_length = length
                        
        print (start, max_length)
        return s[start:start + max_length]