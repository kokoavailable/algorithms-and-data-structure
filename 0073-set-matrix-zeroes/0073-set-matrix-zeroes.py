class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 중간 상태를 저장해놓고, 상태에 따라 전부 반영

        m = len(matrix[0])
        n = len(matrix)

        zero = []

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero.append((i, j))


        for i, j in zero:
            for a in range(m):
                matrix[i][a] = 0
            for b in range(n):
                matrix[b][j] = 0

                    