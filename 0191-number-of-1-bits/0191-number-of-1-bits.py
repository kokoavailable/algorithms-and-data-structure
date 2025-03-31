class Solution:
    def hammingWeight(self, n: int) -> int:
        str_bin_n = str(bin(n)[2:])

        total = 0

        for b in str_bin_n:
            if b == "1":
                total += 1

        return total