class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x_abs = abs(x)
        max_limit = 2**31 - 1 if sign == 1 else 2**31
        reversed_num = 0
        
        while x_abs > 0:
            pop = x_abs % 10
            x_abs = x_abs // 10
            
            if reversed_num > max_limit // 10 or (reversed_num == max_limit // 10 and pop > max_limit % 10):
                return 0
            
            reversed_num = reversed_num * 10 + pop
        
        return reversed_num * sign