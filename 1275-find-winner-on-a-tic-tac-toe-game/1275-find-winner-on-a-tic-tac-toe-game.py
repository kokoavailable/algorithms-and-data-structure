class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        result_grid = [[""] * 3 for _ in range(3)]
        
        def placing_characters(moves):
            turn_flag = 1
            for move in moves:
                x = move[0]
                y = move[1]
                if turn_flag % 2 != 0:    
                    result_grid[x][y] = "X" # turn A
                else:
                    result_grid[x][y] = "O" # turn B
                turn_flag += 1
            
        def check_characters(result_grid):
            for i in range(3):
                if result_grid[i][0] == result_grid[i][1] == result_grid[i][2] != "":
                    return result_grid[i][0]
                if result_grid[0][i] == result_grid[1][i] == result_grid[2][i] != "":
                    return result_grid[0][i]
            # Check diagonals
            if result_grid[0][0] == result_grid[1][1] == result_grid[2][2] != "":
                return result_grid[0][0]
            if result_grid[0][2] == result_grid[1][1] == result_grid[2][0] != "":
                return result_grid[0][2]
            return None
        
        placing_characters(moves)
        winner = check_characters(result_grid)

        if winner == "X":
            return "A"
        elif winner == "O":
            return "B"
        elif len(moves) == 9:
            return "Draw"
        else:
            return "Pending"