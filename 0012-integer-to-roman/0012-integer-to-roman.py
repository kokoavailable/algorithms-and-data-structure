class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        num_dict = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        
        for symbol, value in num_dict.items():
            while num >= value:
                result += symbol  # 로마 숫자를 결과에 추가
                num -= value  # 해당 값만큼 num에서 차감
                
        return result
        