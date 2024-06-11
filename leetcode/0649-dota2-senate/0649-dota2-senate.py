from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        radiant = deque()
        dire = deque()
        
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
                
        n = len(senate)
                
        while radiant and dire:
            r_index = radiant.popleft()
            d_index = dire.popleft()
            
            if r_index < d_index:
                radiant.append(r_index + n)
            else:
                dire.append(d_index + n)
                
        return "Radiant" if radiant else "Dire"
        
        # 선공권자는 뒷사람 죽인다. 그리고 뒤에로 다시 어펜드 된다. 최후의 1인이 남는다면, 그 소속당을 승리당으로 선언한다.
        
        