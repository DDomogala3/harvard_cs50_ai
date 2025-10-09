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

def check_value(board, position):
    x_score = 0
    o_score = 0
    for i,row in enumerate(board):
        for y,z in enumerate(row):
            if (i,y) == position and z == X:
                x_score += 1
            elif (i,y) == position and z == O:
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
    left_bottom = (0,2)
    middle = (1,1)
    bottom_left = (2,2)
    
    
    
    x_score = 0
    o_score = 0          
    diagonal_x = 0
    diagonal_o = 0
    first_row_x = 0
    first_row_o = 0
    diagonal_x += check_value(board,top_left)[0]
    diagonal_x += check_value(board,middle)[0]
    diagonal_x += check_value(board,bottom_left)[0]
    diagonal_o += check_value(board,top_left)[1]
    diagonal_o += check_value(board,middle)[1]
    diagonal_o += check_value(board,bottom_left)[1]
    first_row_x += check_value(board, top_left)[0]
    first_row_o += check_value(board, top_left)[1]
    first_row_x += check_value(board, middle_left)[0]
    first_row_o += check_value(board, middle_left)[1]
    first_row_x += check_value(board, bottom_left)[0]
    first_row_o += check_value(board, bottom_left)[1]
    if diagonal_x == 3:
        return X
    elif diagonal_o == 3:
        return O
    
        
    diagonal_list = []
    diagonal_list.append(check_value(board, top_left))
    diagonal_list.append(check_value(board, middle))
    diagonal_list.append(check_value(board, bottom_left))
    diagonal_x = 0
    diagonal_o = 0
    for i in diagonal_list:
        diagonal_x += i[0]
        diagonal_o += i[1]
    
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
        for i in diagnoal_list:
            tic_tac_score_x += i[0]
            tic_tac_score_y += i[1]
            return tic_tac_score_x, tic_tac_score_y
        
        


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #if game is over because all cells are filled, the funcion should return True
    #return false if game is still in progress
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #utility is 1 if X has won the game, utility is -1 if 0 has won the game
    #utility is called on board if terminal(board) is True
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #positive_infinity = float('inf')
    #negative_infinity = float('-inf')
    #takes board as input and return optimal move for the player on that board
    #the move returned should be optimal action (i,j)
    #if the board is in terminal board, minimax should return None
    raise NotImplementedError
