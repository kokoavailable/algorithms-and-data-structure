class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        length = len(columnTitle)
        result = 0

        for ch in columnTitle:
            result += (ord(ch) - 64) * (26 ** (length - 1))
            print(result)
            length -= 1

        return result