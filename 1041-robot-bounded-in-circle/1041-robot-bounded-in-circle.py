from collections import deque

class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x, y = 0, 0
        
        # 방향 큐: 북(0, 1), 동(1, 0), 남(0, -1), 서(-1, 0)
        directions = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
        
        for instruction in instructions:
            if instruction == 'G':
                dx, dy = directions[0]
                x += dx
                y += dy
            elif instruction == 'L':
                directions.rotate(-1)
            elif instruction == 'R':
                directions.rotate(1)
                
        return (x == 0 and y == 0) or directions[0] != (0, 1)