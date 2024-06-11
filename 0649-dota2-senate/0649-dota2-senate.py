from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        dq = deque((i, c) for i, c in enumerate(senate))
        
        while dq:
            i, c = dq.popleft()
            if c == 'R':
                for j in range(len(dq)):
                    if dq[j][1] == 'D':
                        dq.remove(dq[j])
                        break
                dq.append((i + len(senate), 'R'))
            else:
                for j in range(len(dq)):
                    if dq[j][1] == 'R':
                        dq.remove(dq[j])
                        break
                dq.append((i + len(senate), 'D'))
                
            if not any(x[1] == 'R' for x in dq):
                return "Dire"
            if not any(x[1] == 'D' for x in dq):
                return "Radiant"
        
        # 선공권자는 뒷사람 죽인다. 그리고 뒤에로 다시 어펜드 된다. 최후의 1인이 남는다면, 그 소속당을 승리당으로 선언한다.
        
        