class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        
        
        def backtrack(leds: int, hour:int, minute: int, idx: int):
            if leds == 0:
                if hour < 12 and minute < 60:
                    result.append(f"{hour}:{minute:02d}")
                return
            
            for i in range(idx, 10):
                if i < 4:
                    backtrack(leds - 1, hour + (1 << i), minute, i + 1)
                else:
                    backtrack(leds - 1, hour, minute + (1 << (i - 4)), i + 1)
                    
        backtrack(turnedOn, 0, 0, 0)
        return result
            
            