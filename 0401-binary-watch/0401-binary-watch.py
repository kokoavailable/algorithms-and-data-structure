class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        
        
        def backtrack(leds: int, hour:int, minute: int, idx: int):
            if hour >= 12 or minute >= 60:
                return  # 시간/분 범위를 벗어나면 중단
            
            if leds == 0:
                result.append(f"{hour}:{minute:02d}")
                return
            
            for i in range(idx, 10):
                if i < 4:
                    backtrack(leds - 1, hour + (1 << i), minute, i + 1)
                else:
                    backtrack(leds - 1, hour, minute + (1 << (i - 4)), i + 1)
                    
        backtrack(turnedOn, 0, 0, 0)
        return result
            
        result = []
        
        def backtrack(leds, hours, mins, idx):
            if leds == 0:
                if hours < 12 and minute < 60:
                    result.append
            