class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num_stack = []  
        str_stack = []  
        current_str = ""  
        num = 0  
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                num_stack.append(num)
                str_stack.append(current_str)
                num = 0
                current_str = ""
            elif char == ']':
                repeat_count = num_stack.pop()
                prev_str = str_stack.pop()
                current_str = prev_str + current_str * repeat_count
            else:
                current_str += char
        
        return current_str