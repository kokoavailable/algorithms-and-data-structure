class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""

        while columnNumber != 0:
            columnNumber -= 1
            remain = columnNumber % 26
            result = chr(remain + ord('A')) + result
            columnNumber //= 26

        return result