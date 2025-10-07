class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1] * len(rains)
        dry = []
        visited = {}

        for i, lake in enumerate(rains):
            if lake == 0:
                dry.append(i)
                ans[i] = 1
            else:
                if lake in visited:
                    j = bisect_right(dry, visited[lake])
                    if j == len(dry):
                        return []
                    use = dry.pop(j)
                    ans[use] = lake
                visited[lake] = i
                ans[i] = -1

        return ans 