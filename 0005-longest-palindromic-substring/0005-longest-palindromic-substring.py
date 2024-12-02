class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        # DP 테이블 초기화
        dp = [[False] * n for _ in range(n)]

        # 가장 긴 팰린드롬의 시작점과 길이
        start = 0
        max_length = 0

        # 길이 1 팰린드롬 초기화
        for i in range(n):
            dp[i][i] = True
            start = i
            max_length = 1

        # 길이 2 팰린드롬 초기화
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2

        # 길이 3 이상의 팰린드롬 확인
        for length in range(3, n + 1):  # length는 부분 문자열의 길이
            for i in range(n - length + 1):
                j = i + length - 1  # 끝 인덱스
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_length = length

        # 가장 긴 팰린드롬 부분 문자열 반환
        return s[start:start + max_length]
    
    
        dp = [[False]* n for _ in range(n)]
        
        start = 0
        max_length = 0
        
        for i in range(n):
            dp[i][i] = True
            start = i
            max_length = 1
            
        for i in range(n -1):
            if s[i] == s[i+1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2
                
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i]  == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_length = length
                    
        return s[start:start + max_length]
                