class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        dry = []
        last = {}

        for i, lake in enumerate(rains):
            if lake == 0:
                dry.append(i)
                ans[i] = 1
            else:
                if lake in last:
                    j = bisect_right(dry, last[lake])
                    if j == len(dry):
                        return []
                    use = dry.pop(j)
                    ans[use] = lake
                last[lake] = i
                ans[i] = -1
        
        return ans