#from tictactoe import *
from tictactoe_duck_work import *
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
board12 = [[EMPTY, "O", "X"],
            [EMPTY, EMPTY, "O"],
            ["X", "O", "O"]]
print("This is the next move %s." % player(board1))
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
#for i in diagonal_list:
#    diagonal_x += i[0]
#    diagonal_o += i[1]
#print(diagonal_x)
#print(diagonal_o)
#testing


diagonal_list_test = [top_left,middle,bottom_left]
opposite_diagonal_list_test = [right_top,middle,bottom_left]
first_column_list_test = [top_left, middle_left, bottom_left]
middle_column_list_test = [left_middle, middle,bottom_middle]
third_column_list_test = [right_top, right_middle,bottom_right]
top_row_list_test = [top_left,left_middle,right_top]
middle_row_list_test = [middle_left,middle,right_middle]
bottom_row_list_test = [bottom_left, bottom_middle,bottom_right]
#print(check_value(board4, diagonal_list_test))
#print(winner(board4))
#print(winner(board5))
#print(winner(board3))
#print(terminal(board4))
#print(terminal(board5))

#print("MAX board 5: %d " % MAX(board5))
#print("MAX board 5: %d " % MIN(board5))
#print("MAX board 7: %d " % MAX(board7))
#print("MIN board 7: %d" % MIN(board7))
#print("MIN board 8: %d" % MIN(board8))
#print("MAX board 8: %d" % MAX(board8))
#print("MIN board 9: %d" % MIN(board9))
#print("MAX board 9: %d" % MAX(board9))

#print(minimax(board7))
#print(minimax(board8))
#print(utility(board8))
print(MAX(board11))
print(utility(board10))

print("Winner board 11 %s." % winner(board11))
print(check_value(board11,opposite_diagonal_list_test))
print(player(board10))
for action in actions(board11):
    new_result = (result(board11,action))
    print(utility(new_result))
    if utility(new_result) < utility(result(board11,action)):
        print(utility(new_result))
value_list = []
value_list.append(check_value(board11,diagonal_list_test))
value_list.append(check_value(board11,first_column_list_test))
value_list.append(check_value(board11,middle_column_list_test))
value_list.append(check_value(board11,third_column_list_test))
value_list.append(check_value(board11,top_row_list_test))
value_list.append(check_value(board11, middle_row_list_test))
value_list.append(check_value(board11, bottom_row_list_test))
value_list.append(check_value(board11,opposite_diagonal_list_test))



for i in value_list:
    if i[0] == 3:
        print(X)
    elif i[1] == 3:
        print(O)
def winner_two(board):
    top_left = (0,0)
    middle_left = (1,0)
    bottom_left = (2,0)
    left_middle = (0,1)
    right_top = (0,2)
    right_middle = (1,2)
    middle = (1,1)
    bottom_middle = (2,1)
    bottom_right = (2,2)
    top_middle = (0,1)
    diagonal_list_test = [top_left,middle,bottom_right]
    opposite_diagonal_list_test = [right_top,middle,bottom_left]
    first_column_list_test = [top_left, middle_left, bottom_left]
    middle_column_list_test = [left_middle, middle,bottom_middle]
    third_column_list_test = [right_top, right_middle,bottom_right]
    top_row_list_test = [top_left,left_middle,right_top]
    
    middle_row_list_test = [middle_left,middle,right_middle]
    bottom_row_list_test = [bottom_left, bottom_middle,bottom_right]
    
    
    value_list = []
    value_list.append(check_value(board,diagonal_list_test))
    value_list.append(check_value(board,opposite_diagonal_list_test))
    value_list.append(check_value(board,first_column_list_test))
    value_list.append(check_value(board,middle_column_list_test))
    value_list.append(check_value(board,third_column_list_test))
    value_list.append(check_value(board,top_row_list_test))
    value_list.append(check_value(board, middle_row_list_test))
    value_list.append(check_value(board, bottom_row_list_test))
    for i in value_list:
        if i[0] == 3:
            return X
        elif i[1] == 3:
            return O

print(winner_two(board11))
print(winner(board11))
print(MAX(board8))
print(MAX(board12))
print(MAX(board10))
print(MAX(board8))
print(MIN(board7))
