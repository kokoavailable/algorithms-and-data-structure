class Solution:
    def removeStars(self, s: str) -> str:
        ls_s = list(s)
        ls_s.reverse()
        result = []
        star_count = 0
        
        
        for char in ls_s:
            if star_count > 0 and char != '*':
                star_count -= 1
                continue
                
            if char == '*':
                star_count += 1
            else:
                result.append(char)
            
        result.reverse()
                
        return "".join(result)