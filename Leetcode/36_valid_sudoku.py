from collections import Counter
import math

# Given a Counter, returns true or false whether or not there is
# more than one occurrence of a number.
def isValidSection(counter):
    most_occur = counter.most_common(2)
    # . is the empty part of the grid so it should occur often.
    # But there can be a case where the entire section could be filled.
    if most_occur[0][0] != "." and most_occur[0][1] > 1:
        return False
    # Can be a scenario where the entire section is "empty," or filled with ".", so the len has
    # to be graeter than 1.
    elif len(most_occur) > 1 and most_occur[1][1] > 1:
        return False
    return True

# A valid subgrid is an integer of the square root of the size.
# Takes the sqrt of the length of the board then does the power of 2
# and checks if it's the same length as the original.
def isValidSubgrid(board):
    return math.sqrt(len(board)) ** 2 == len(board)

# Puts all the columns of the board into an array and returns it.
def transposeGrid(board):
    cols = []
    for i in range(len(board)):
        col = []
        for j in range(len(board)):
            col.append(board[j][i])
        cols.append(col)
    return cols

def getSubgrid(board):
    subgrid = []
    subgrid_size = int(math.sqrt(len(board)))
    # The iterable jumps by the subgrid size each loop.
    for col in range(0, len(board), subgrid_size):
        for row in range(0, len(board), subgrid_size):
            grid = []
            for i in range(subgrid_size):
                for j in range(subgrid_size):
                    # (row, col) defines the top-left corner of the subgrid, and 
                    # (i, j) is a local coordinate offset within the subgrid, scanning
                    # through each cell, row-by-row. This definition means that (row i, col + j)
                    # is effecitevly a translation from a local to a global coordinate on the 
                    # entire grid that defines the position of the subgrid cell.
                    grid.append(board[col + i][row + j])
            subgrid.append(grid)
    return subgrid

def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Returns false right away if the subgrid is not valid.
    # A valid subgrid would need to be a perfect square root of the size 
    # of the entire board. If not the sudoku grid isn't solvable.
    if not isValidSubgrid(board):
        return False

    # Gets all the columns and subgrids of the board.
    cols = transposeGrid(board)
    subgrids = getSubgrid(board)

    for i in range(len(board)):
        # Counts the occurrences of items within the list.
        # Numbers and the empty "."
        # If any number has more than one occurrence, whether
        # in the row, column, or subgrid,
        # the sudoku grid is not valid as it violates the sudoku rules.
        row_counter = Counter(board[i])
        col_counter = Counter(cols[i])
        subgrid_counter = Counter(subgrids[i])

        if not (isValidSection(row_counter) and isValidSection(col_counter) and isValidSection(subgrid_counter)):
            return False

    return True