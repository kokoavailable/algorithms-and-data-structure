class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0  # 필요한 비트 반전의 총 개수

        while a > 0 or b > 0 or c > 0:
            # 각 숫자의 최하위 비트 추출
            a_bit = a & 1
            b_bit = b & 1
            c_bit = c & 1

            # 조건에 따른 비트 반전 계산
            if c_bit == 0:
                # c_bit이 0이면, a_bit와 b_bit 모두 0이어야 함
                flips += a_bit + b_bit  # 둘 다 0이 아니라면 뒤집기
            else:
                # c_bit이 1이면, a_bit나 b_bit 중 하나는 1이어야 함
                if a_bit == 0 and b_bit == 0:
                    flips += 1  # 둘 다 0이면 하나를 1로 뒤집기

            # 숫자를 오른쪽으로 한 비트씩 이동 (다음 비트를 비교)
            a >>= 1
            b >>= 1
            c >>= 1

        return flips