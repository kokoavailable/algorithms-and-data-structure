class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        # dx dy가 일정한가.
        
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        if x1 - x0 == 0:
            slope = float('inf')
        else:
            slope = (y1 - y0) / float(x1 - x0)
        
        for i in range(1, len(coordinates) - 1):
            x0, y0 = coordinates[i]
            x1, y1 = coordinates[i + 1]
            
            if x1 - x0 == 0:
                current_slope = float('inf')
            else:
                current_slope = (y1 - y0) / float(x1 - x0)

                
            if current_slope != slope:
                return False
            
        return True
            
            