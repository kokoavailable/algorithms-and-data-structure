class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        current_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]
            
            # 현재 연료가 부족하면 다음 주유소를 새로운 시작점으로 설정
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0
        
        # 전체 연료가 비용보다 적으면 순회 불가
        return start_index if total_tank >= 0 else -1