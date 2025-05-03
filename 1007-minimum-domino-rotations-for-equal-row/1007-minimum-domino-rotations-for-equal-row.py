class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        cnt_tops = Counter(tops)
        cnt_bottoms = Counter(bottoms)
        n = len(tops)
        
        m = 0
        candidate = -1  # 최빈값이자 후보 숫자
        
        # 후보 숫자 찾기 (1~6 중에서)
        for i in range(1, 7):
            if cnt_tops[i] + cnt_bottoms[i] >= n:
                candidate = i
                break  
        
        if candidate == -1:
            return -1  # 어떤 숫자로도 통일 불가
        
        rotate_top = 0
        rotate_bottom = 0
        
        for i in range(n):
            if tops[i] != candidate and bottoms[i] != candidate:
                return -1  # 이 도미노에 candidate가 아예 없음 → 불가능
            elif tops[i] != candidate:
                rotate_top += 1
            elif bottoms[i] != candidate:
                rotate_bottom += 1
        
        return min(rotate_top, rotate_bottom)
