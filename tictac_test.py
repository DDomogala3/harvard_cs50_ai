from tictactoe import *
from tictac_ext import count_board
EMPTY = None
X = "X"
O = "O"
board1 = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
board2 = [[EMPTY, "X", "O"],
           [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
board3 = [[EMPTY, "X", "O"],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
board4 = [["X", "X", "O"],
            ["O", "X", "O"],
            ["X", "X", "X"]]
board5 = [["X", "X", "O"],
            ["O", "X", "O"],
            ["X", EMPTY, "O"]]

print("This is the next move %s." % player(board1))
player(initial_state())
actions(board4)
print(result(board5,(2,1)))
print(winner(board4))
top_left = (0,0)
middle = (1,1)
bottom_left = (2,2)
print(check_value(board4,top_left)[0])
print(check_value(board4,middle)[0])
print(check_value(board4,bottom_left)[0])
