class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        new_ls = [tuple(sorted(domino)) for domino in dominoes]
        
        cnt_dominoes = Counter(new_ls)
        
        answer = 0
        for v in cnt_dominoes.values():
            answer += v * (v - 1) // 2
        
        return answer