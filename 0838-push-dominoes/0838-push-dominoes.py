class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # 시간 흐름, 상태 변화, 상호작용 시뮬레이션/ 상태 전이
        # 양방향을 생각해야함
        # 중립성 판단, 거리기반

        n = len(dominoes)
        forces = [0] * n

        #(R)
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] += force

        #(L)
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] -= force 

        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')
        
        return ''.join(result)