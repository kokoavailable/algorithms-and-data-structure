class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransome_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        for char, cnt in ransome_count.items():
            if magazine_count[char] < cnt:
                return False
            
        
        return True