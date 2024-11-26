class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        
        m = len(potions)
        result = []
        
        for spell in spells:
            target = (success + spell - 1) // spell
            idx = bisect_left(potions, target)
            result.append(m - idx)
                    
        return result