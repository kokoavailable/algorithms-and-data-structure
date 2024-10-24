class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def binary_search(house):
            left, right = 0, len(heaters) -1
            while left <= right:
                mid = (left + right) // 2
                if heaters[mid] == house:
                    return mid
                elif heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        min_radius = 0
        
        for house in houses:
            pos = binary_search(house)
            
            if pos == 0:
                closest_distance = abs(heaters[0] - house)
            elif pos == len(heaters):
                closest_distance = abs(heaters[-1] - house)
            else:
                closest_distance = min(abs(heaters[pos] - house), abs(heaters[pos - 1] - house))
        
            min_radius = max(min_radius, closest_distance)
        
        return min_radius