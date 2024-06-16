class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 인덱스에 따라서 해당 문자저장해놓고, 세개씩 보여주면 되잖아 . 조합으로. 근데 이건 브루트 포스인데
        
        if not digits:
            return []
        
        # 숫자에 대응되는 문자 매핑 리스트
        alphabet_list = [
            [], [], ['a', 'b', 'c'], ['d', 'e', 'f'], 
            ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], 
            ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']
        ]
        
        # 초기 결과 리스트
        result = [""]
        
        # 각 숫자에 대해 반복
        for digit in digits:
            number = int(digit)
            new_result = []
            
            # 현재 숫자에 해당하는 문자들을 가져옴
            possible_chars = alphabet_list[number]
            
            # 기존 결과에 새 문자 추가
            for combination in result:
                for char in possible_chars:
                    new_result.append(combination + char)
            
            # 결과 업데이트
            result = new_result
        
        return result