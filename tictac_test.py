from tictactoe import *
from tictac_ext import count_board
EMPTY = "EMPTY"
X = "X"
O = "O"
board1 = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
board2 = [[EMPTY, "X", "O",
           EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
board3 = [[EMPTY, "X", "O"],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
board4 = [["X", "X", "O"],
            ["O", "X", "O"],
            ["X", "X", "O"]]
player(board4)
