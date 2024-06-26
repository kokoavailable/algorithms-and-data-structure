class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for char in s:
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char
                
        return result
            
        