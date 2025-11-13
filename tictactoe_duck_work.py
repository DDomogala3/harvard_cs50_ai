"""
Tic Tac Toe Player
"""

import math
from tictac_ext import count_board
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if count_board(board)[3] == 0:
        return X
    elif count_board(board)[0] > count_board(board)[1] and count_board(board)[3] < 9:
        return O
    elif count_board(board)[0] < count_board(board)[1] and count_board(board)[3] < 9:
        return X
    elif count_board(board)[0] == count_board(board)[1] and count_board(board)[3] < 9:
        return X
    elif count_board(board)[3] == 9:
        print("FULL")
    #returns which players turn it is
   # raise NotImplementedError
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    coordinate_set = []
    for i,row in enumerate(board):
        #print(i)
        #print(row)
        for y,z in enumerate(row):
            if z == None:
                print(i,y)
                coordinate_set.append((i,y))
    return coordinate_set
                
            
    #returns set of actions that can be taken on a board
    #each action should be reported as a tuple
    
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #if action is not valid, raise an  exception
    #original board should be left unmodified
    
    for i,row in enumerate(board):
        for y,z in enumerate(row):
            if (i,y) == action:
                new_board = copy.deepcopy(board)
                for i,row in enumerate(new_board):
                    for y,z in enumerate(row):
                        if (i,y) == action:
                            print(player(board))
                            new_board[i][y] = player(board)
                        
    return new_board
    #raise NotImplementedError

def check_value(board, position_list):
    x_score = 0
    o_score = 0
    for i,row in enumerate(board):
        for y,z in enumerate(row):
            if (i,y) == position_list[0] and z == X:
                x_score += 1
            elif (i,y) == position_list[0] and z == O:
                o_score += 1
            elif (i,y) == position_list[1] and z == X:
                x_score += 1
            elif (i,y) == position_list[1] and z == O:
                o_score += 1
            elif (i,y) == position_list[2] and z == X:
                x_score += 1
            elif (i,y) == position_list[2] and z == O:
                o_score += 1
    return x_score, o_score
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check diagonals check elements at indices (0,0), (1,0), (2,2)
    #if no winner, return None

        
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
            
  
    #return winner_list
    
    #raise NotImplementedError

class Assess(object):
    
    ''''A way to keep score of the board'''
    def init(self,board, position , tictac_list, tic_tac_score_x,tic_tac_score_y):
        '''Features of the board and scoring.'''
        self.board = board
        self.tictac_list = tictac_list
        self.tic_tac_score = tic_tac_score
    def check_value(self,board, position):
        x_score  = 0
        o_score = 0
        for i, row in enumerate(board):
            for y, z in enumerate(row):
                if (i,y) == position and z == X:
                    x_score += 1
                elif (i,y) == position and z == O:
                    o_score += 1
            return x_score, o_score
    def score_value(self,tictac_list, tic_tac_score_x,tic_tac_score_y):
        for i in tictac_list:
            tic_tac_score_x += i[0]
            tic_tac_score_y += i[1]
            return tic_tac_score_x, tic_tac_score_y
        
        


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #if game is over because all cells are filled, the funcion should return True
    #return false if game is still in progress
    if count_board(board)[3] == 9:
        return True
    elif count_board(board)[3] < 9:
        return False
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #utility is 1 if X has won the game, utility is -1 if 0 has won the game
    #utility is called on board if terminal(board) is True
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    #raise NotImplementedError
#define MAX
def MAX(board):
    #find the best move for the maximizing player
  
    max_utility = float('-inf')
    for action in actions(board):
        X_result = result(board,action)
            #return max result
        print("This is the utility function %d." % utility(X_result))  
        #max_utility = max(max_utility, utility(X_result))
        #best_action = action   
        if max_utility < utility(X_result):
            max_utility = utility(X_result)
            best_action = action
    return max_utility, best_action  
    
         
def MIN(board):
    min_utility = float('inf')
    for action in actions(board):
        O_result = result(board,action)

        print("This is the utility function %d." % utility(O_result))
        if min_utility > utility(O_result):
            min_utility = utility(O_result)
            best_action = action
    return min_utility, best_action
  
        
    #return maximum value
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #positive_infinity = float('inf')
    #negative_infinity = float('-inf')
    #takes board as input and return optimal move for the player on that board
    #the move returned should be optimal action (i,j)
    #if the board is in terminal board, minimax should return None
    #max
  #  def Max_VALUE(board):
   #     v = float('-inf')
    #    if terminal(board) == False:
       #     return utility(board)
    #    else:
    #        return None 
     #   V = float('-inf')
     #   for action in actions(board):
     #       v = max(v, MIN(result(board,action)))
    #    return v
    for action in actions(board):
        
        test_result = result(board,action)
        if MAX(test_result) >= utility(test_result):
            print("MAX test result %d." % MAX(test_result))
            print("utility test result %d." % utility(test_result))
            new_action = action
            return new_action
        
            
  #  if MAX(test_result) >= utility(test_result):
    #    print("Max test result %d" % MAX(test_result))
      #  print("Utility test result %d." % utility(test_result))
      #  for action in actions(test_result):
       #     return action
    #return (MAX(board))    
    #raise NotImplementedError
