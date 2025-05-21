class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 중간 상태를 저장해놓고, 상태에 따라 전부 반영

        m = len(matrix[0])
        n = len(matrix)

        zero_cols = set()
        zero_rows = set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)



        for i in zero_rows:
            for j in range(m):
                matrix[i][j] = 0

        for j in zero_cols:
            for i in range(n):
                matrix[i][j] = 0

                    