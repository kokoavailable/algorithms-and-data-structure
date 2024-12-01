class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        arrows = 1 
        current_end = points[0][1]

        for x_start, x_end in points:
            if x_start > current_end:
                arrows += 1
                current_end = x_end 

        return arrows