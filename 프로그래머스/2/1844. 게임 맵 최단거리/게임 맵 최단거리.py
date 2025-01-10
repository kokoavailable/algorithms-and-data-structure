from collections import deque

def solution(maps):
    m, n = len(maps), len(maps[0])
    
    queue = deque([(0, 0, 1)])
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    visited = [[False] * n for _ in range(m)]
    visited[0][0] = True
    
    while queue:
        x, y, dist = queue.popleft()
        
        if x == m - 1 and y == n - 1:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    
    return -1