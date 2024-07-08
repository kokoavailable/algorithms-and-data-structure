class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        
        result = [0] * (len(num1) + len(num2))
        
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                sum = mul + result[i + j + 1]
                result[i + j + 1] = sum % 10
                result[i + j] += sum // 10
                
        result_str = ''.join(map(str, result)).lstrip('0')
        
        return result_str if result_str else '0'
                
        