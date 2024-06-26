class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        current_position = [0, 0]
        
        for move in moves:
            if move == 'L':
                current_position[0] -= 1
            if move == 'R':
                current_position[0] += 1
            if move == 'U':
                current_position[1] += 1
            if move == 'D':
                current_position[1] -= 1
        
        return current_position == [0, 0]
                
        
            