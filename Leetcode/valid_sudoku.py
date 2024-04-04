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
    if math.sqrt(len(board)) ** 2 == len(board):
        return True
    return False

# Puts all the columns of the board into an array and returns it.
def getCol(board):
    full_col = []
    for i in range(len(board)):
        col = []
        for j in range(len(board)):
            col.append(board[j][i])
        full_col.append(col)
    return full_col

def getSubgrid(board):
    subgrid = []
    # The iterable jumps by the subgrid size each loop.
    for col in range(0, len(board), int(math.sqrt(len(board)))):
        for row in range(0, len(board[0]), int(math.sqrt(len(board[0])))):
            grid = []
            for i in range(int(math.sqrt(len(board)))):
                for j in range(int(math.sqrt(len(board)))):
                    # Since the iterable jumps by the subgrid size, adding one to the
                    # iterable each loop will go through the subgrid.
                    grid.append(board[col + i][row + j])
            subgrid.append(grid)
    return subgrid

def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Returns false right away if the subgrid is not valid
    # meaning the sudoku grid isn't solvable.
    if not isValidSubgrid(board):
        return False

    # Gets all the columns and subgrids of the board.
    full_col = getCol(board)
    subgrid = getSubgrid(board)

    for i in range(len(board)):
        # Counts the occurrences of items within the list.
        # Numbers and the empty "."
        # If any occurence other than "." is greater than 1, it 
        # should return false.
        row_counter = Counter(board[i])
        if not isValidSection(row_counter):
            return False
        
        col_counter = Counter(full_col[i])
        if not isValidSection(col_counter):
            return False
        
        subgrid_counter = Counter(subgrid[i])
        if not isValidSection(subgrid_counter):
            return False

    return True