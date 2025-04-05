class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        num = 0
        sign = 1
        i = 0

        while i < len(s):
            char = s[i]
            if char.isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                res += sign * num
                continue
            elif char == '+':
                sign = 1
            elif char == '-':
                sign = -1
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif char == ')':
                prev_sign = stack.pop()
                prev_res = stack.pop()
                res = prev_res + prev_sign * res
            
            i += 1
        
        return res