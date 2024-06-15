class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        # 현재 위치에서 외곽을 향해 간다. 컬럼이나 행이 0 인점
        # 현재 위치에서 벽은 제외, 현재 위치 이전의 위치에 지나 갔떤 자리는 제외 
        m, n = len(maze), len(maze[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set()
        visited.add((entrance[0], entrance[1]))
        
        while queue:
            x, y, steps = queue.popleft()
            
            if (x == 0 or y == 0 or x == m-1 or y == n-1) and (x != entrance[0] or y != entrance[1]):
                return steps
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.' and (nx, ny) not in visited:
                    queue.append((nx, ny, steps + 1))
                    visited.add((nx, ny))
                    
        return -1