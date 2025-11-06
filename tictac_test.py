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

board6 = [["O", "X", "O"],
            ["O", "O", "O"],
            ["X", "X", "O"]]
print("This is the next move %s." % player(board1))
player(initial_state())
actions(board4)
print(result(board5,(2,1)))

top_left = (0,0)
middle = (1,1)
bottom_left = (2,2)



diagonal_x = 0
diagonal_o = 0
#for i in diagonal_list:
#    diagonal_x += i[0]
#    diagonal_o += i[1]
#print(diagonal_x)
#print(diagonal_o)
#testing


diagonal_list_test = [top_left,middle,bottom_left]
print(check_value(board4, diagonal_list_test))
print(winner(board4))
print(winner(board5))
