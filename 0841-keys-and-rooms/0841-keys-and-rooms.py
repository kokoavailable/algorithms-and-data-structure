from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # 인덱스 0인 방 무조건 방문, 그리고 거기서 순차적으로 모든 키(인덱스)들을 순회했을떄
        # 순회가 안된 방이 있으면, false를 반환한다.
        
        visited = set()
        queue = deque([0])
        
        while queue:
            room = queue.popleft()
            visited.add(room)
            
            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)
            
#         while stack:
#             room = stack.pop()
#             if room not in visited:
#                 visited.add(room)
#                 for key in rooms[room]:
#                     if key not in visited:
#                         stack.append(key)
                        
#         def dfs(room):
#             visited.add(room)
#             for key in rooms[room]:
#                 if key not in visited:
#                     dfs(key)
                    
#         visited = set()
#         dfs(0)
                
                
        return len(visited) == len(rooms)
            