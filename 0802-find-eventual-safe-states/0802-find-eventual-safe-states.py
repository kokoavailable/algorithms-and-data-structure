class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 현노드에서 아웃고잉 노드가 없거나 최소 내가 뻗는 모든 노드에서 아웃 고잉 노드가 없어야함.
        n = len(graph)
        color = [0] * n

        def dfs(node):
            if color[node] > 0:
                return color[node] == 2 
            color[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            color[node] = 2 
            return True

        return [i for i in range(n) if dfs(i)]