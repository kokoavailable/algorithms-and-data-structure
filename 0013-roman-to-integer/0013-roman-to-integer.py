class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0
        
        for i in range(len(s) - 1):
            if s[i] == 'C' and s[i+1] in ["D", "M"]:
                answer -= 100
                continue
            elif s[i] == 'X' and s[i+1] in ["L", "C"]:
                answer -= 10
                continue
            elif s[i] == 'I' and s[i+1] in ["V", "X"]:
                answer -= 1
                continue
            
            if s[i] == "I":
                answer += 1
            elif s[i] == "V":
                answer += 5
            elif s[i] == "X":
                answer += 10
            elif s[i] == "L":
                answer += 50
            elif s[i] == "C":
                answer += 100
            elif s[i] == "D":
                answer += 500
            elif s[i] == "M":
                answer += 1000
                
            
        if s[-1] == "I":
            answer += 1
        elif s[-1] == "V":
            answer += 5
        elif s[-1] == "X":
            answer += 10
        elif s[-1] == "L":
            answer += 50
        elif s[-1] == "C":
            answer += 100
        elif s[-1] == "D":
            answer += 500
        elif s[-1] == "M":
            answer += 1000
            
        return answer 