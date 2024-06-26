class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        
        for move in moves:
            if move == 'L':
                x -= 1
            if move == 'R':
                x += 1
            if move == 'U':
                y += 1
            if move == 'D':
                y -= 1
        
        return x == 0 and y == 0
                
        
            