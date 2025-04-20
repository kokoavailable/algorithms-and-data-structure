class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        max_points = 0

        for i in range(n):
            slope_count = defaultdict(int)
            same_points = 1
            curr_max = 0

            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                if dx == 0 and dy == 0:
                    same_points += 1
                    continue

                if dx == 0:
                    slope = ('inf', 0)
                else:
                    g = gcd(dy, dx)
                    dy //= g
                    dx //= g

                    if dx < 0:
                        dy *= -1
                        dx *= -1

                    slope = (dy, dx)

                slope_count[slope] += 1
                curr_max = max(curr_max, slope_count[slope])

            max_points = max(max_points, curr_max + same_points)

        return max_points