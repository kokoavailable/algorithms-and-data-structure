class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        guess = x // 2
        while guess * guess > x:
            guess = (guess + x // guess) // 2
        
        return guess