class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        len_s = len(s)
        
        for i in range(1, len_s // 2 + 1):
            if len_s % i == 0:
                substring = s[:i]
                if substring * (len_s // i) == s:
                    return True
        