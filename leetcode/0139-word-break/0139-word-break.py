class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # dictionary words 를 재사용할 수 있다.. 
        # 가능한 조합들을 다 생각해봐야할 것 같은데..
        # 일단 브루트포스를 생각해보자.
        word_set = set(wordDict)
        
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] == True and s[j:i] in word_set:
                    dp[i] = True
                    break
                    
        return dp[len(s)]