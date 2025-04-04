class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)

        for u, v in redEdges:
            red_graph[u].append(v)
        for u, v in blueEdges:
            blue_graph[u].append(v)

        dist = [[float('inf')] * 2 for _ in range(n)]
        dist[0][0] = dist[0][1] = 0
        
        q = deque()
        q.append((0, 0))  # Start with red
        q.append((0, 1))  # Start with blue

        visited = set()
        visited.add((0, 0))
        visited.add((0, 1))


        while q:
            node, color = q.popleft()
            next_color = 1 - color
            next_graph = blue_graph if color == 0 else red_graph

            for neighbor in next_graph[node]:
                if (neighbor, next_color) not in visited:
                    dist[neighbor][next_color] = dist[node][color] + 1
                    visited.add((neighbor, next_color))
                    q.append((neighbor, next_color))
        
        res = []
        for red_d, blue_d in dist:
            min_dist = min(red_d, blue_d)
            res.append(min_dist if min_dist != float('inf') else -1)
        
        return res