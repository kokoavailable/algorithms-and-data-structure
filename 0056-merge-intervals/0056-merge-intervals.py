class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        result = []
        
        start = intervals[0][0]
        end = intervals[0][1]
        
        for interval in intervals:
            if end >= interval[0]:
                end = max(end, interval[1])
            else:
                result.append([start, end])
                start = interval[0]
                end = interval[1]
                
        result.append([start, end])
        
        return result