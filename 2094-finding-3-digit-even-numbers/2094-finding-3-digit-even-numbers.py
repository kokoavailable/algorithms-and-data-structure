class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # 디짓 리스트를 조합해서 숫자를 만든다.. 
        # 1. 리딩 제로가 아닐것
        # 2. 짝수일것
        # 3. 세개를 조합한 숫자일 것.
        # 4. 조합해 append 해서 return

        digits.sort()
        n = len(digits)
        result = []

        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                for k in range(n):
                    if digits[k] % 2 != 0:
                        continue
                    
                    if i == j or j == k or i == k:
                        continue

                    total = digits[i] * 100 + digits[j] * 10 + digits[k]
                    result.append(total)

        result = list(set(result))
        result.sort()

        return result


