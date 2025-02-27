class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        target = n * n
        
        visited = {}
        queue = deque()
        queue.append((1, 0))
        visited[1] = 0
        
        while queue:
            curr, steps = queue.popleft()
            if curr == target:
                return steps
            for i in range(1, 7):
                next_step = curr + i
                if next_step > target:
                    continue
                s = next_step - 1
                row = s // n
                original_row = (n - 1) - row
                col_in_row = s % n
                row_from_bottom = row
                if row_from_bottom % 2 == 0:
                    col = col_in_row
                else:
                    col = (n - 1) - col_in_row
                if board[original_row][col] != -1:
                    next_step = board[original_row][col]
                if next_step == target:
                    return steps + 1
                if next_step not in visited:
                    visited[next_step] = steps + 1
                    queue.append((next_step, steps + 1))
        return -1