from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_counter = Counter(board[i])
            for key in row_counter:
                if key != "." and row_counter[key] > 1:
                    return False
            
            col = []
            for j in range(9):
                col.append(board[j][i])
            col_counter = Counter(col)
            for key in col_counter:
                if key != "." and col_counter[key] > 1:
                    return False
        
        for col in range(0, 9, 3):
            for row in range(0, 9, 3):
                subgrid = []
                for i in range(3):
                    for j in range(3):
                        subgrid.append(board[col + i][row + j])
                    subgrid_counter = Counter(subgrid)
                    for key in subgrid_counter:
                        if key != "." and subgrid_counter[key] > 1:
                            return False

        return True
