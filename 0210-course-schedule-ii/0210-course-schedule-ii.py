class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 인접 리스트(이중리스트)와 차수 리스트 
        # graph = {i: [] for i in range(numCourses)}
        adj = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses

        # b가 선행 노드 
        for a, b in prerequisites:
            adj[b].append(a)
            in_degree[a] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []

        while queue:
            curr = queue.popleft()
            order.append(curr)
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) == numCourses:
            return order
        else:
            return []