#from tictactoe import *
from tictactoe_duck_work_min_max_11232025 import *
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
            [EMPTY, "O", EMPTY]]
board4 = [["X", "X", "O"],
            ["O", "X", "O"],
            ["X", "X", "X"]]
board5 = [["X", "X", "O"],
            ["O", "X", "O"],
            ["X", EMPTY, "O"]]

board6 = [["O", "X", "O"],
            ["O", "O", "O"],
            ["X", "X", "O"]]
board7 = [["O", "X", EMPTY],
            ["O", "O", "X"],
            ["X", "X", EMPTY]]
board8 = [["O", EMPTY, "X"],
            [EMPTY, "O", "O"],
            ["X", "X", EMPTY]]
board9 = [["O", "O", "X"],
            [EMPTY, "X", "O"],
            ["O", "X", EMPTY]]
board10 = [[EMPTY, "O", "O"],
            ["X", EMPTY, "X"],
            ["O", "X", "O"]]
board11 = [[EMPTY, "O", "X"],
            [EMPTY, "X", "O"],
            [EMPTY, "O", "O"]]
board12 = [["X", "O", "X"],
            [EMPTY, EMPTY, "O"],
            ["X", "O", "O"]]
board13 = [["X", EMPTY, "O"],
            [EMPTY, "O", EMPTY],
            [EMPTY, EMPTY, "X"]]
board14 = [["X", "X", "O"],
            [EMPTY, "O", EMPTY],
            [EMPTY, EMPTY, EMPTY]]
board15 = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, "O", EMPTY],
            ["O", "X", "X"]]
#print("This is the next move %s." % player(board1))
player(initial_state())
actions(board4)
#print(result(board5,(2,1)))


top_left = (0,0)
middle_left = (1,0)
bottom_left = (2,0)
left_middle = (1,0)
right_top = (0,2)
right_middle = (1,2)
middle = (1,1)
bottom_middle = (2,1)
bottom_right = (2,2)
top_middle = (0,1)
    


diagonal_x = 0
diagonal_o = 0

#print(MAX(board12,float('-inf'),float('inf')))
#print(MIN(board4))
print(MIN(board14,float('-inf'),float('inf')))
print(MAX(board14,float('-inf'),float('inf')))
#print(MAX(board12,float('-inf'),float('inf')))
print(minimax(board14))
#print(actions(board13))
#print(player(board13))
#print(MAX(board13,float('-inf'),float('inf')))

for action in actions(board14):
    X_result = result(board13,action)
    print(X_result,utility(X_result))
#for action in actions(board12):
#    X_result = result(board12,action)
 #   min_utility = float('inf')
#    MIN_v = min(min_utility,utility(X_result))
#print(MIN_v)
#mutumbo
print(actions(board15))
for action in actions(board14):
	#print(utility(result(board15,action)))
	X_result = result(board14,action)
	#save new_board
	if utility(X_result) == 0:
		O_result = result(X_result,action)
	if utility(O_result) == -1:
		print(O_result,action)
def mutumbo(board,player):
	if player == "O":
		for action in actions(board):
			O_result = result(board,action)
			if utility(O_result) == 0:
				X_result = result(O_result,action)
				#me no likey
			if utility(X_result) == 1:
			
				return X_result,action
	elif player == "X":
		for action in actions(board):
			X_result = result(board,action)
	#save new_board
			if utility(X_result) == 0:
				O_result = result(X_result,action)
			if utility(O_result) == -1:
				
				return (O_result,action)
						
print(mutumbo(board13,"X"))
print(minimax(board5))