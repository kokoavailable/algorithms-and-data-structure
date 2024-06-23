class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set("aeiouAEIOU") # 모음 집합
        
        # initial window
        window = s[:k]
        cnt = sum(1 for char in window if char in vowels)
        result = cnt
        
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                cnt -= 1
            if s[i] in vowels:
                cnt += 1
            result = max(result, cnt)
            
        return result
            
            
            