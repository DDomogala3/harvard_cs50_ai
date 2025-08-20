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


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check diagonals check elements at indices (0,0), (1,0), (2,2)
    #if no winner, return None
    top_left = (0,0)
    middle = (1,0)
    bottom_left = (2,2)
    x_score = 0
    for i, row in enumerate(board):
        for y,z in enumerate(row):
            if (y,i) == top_left and z == X:
               x_score += 1
            elif (y,i) == middle and z == X:
                x_score += 1
            elif (y,i) == bottom_left and z == X:
                x_score += 1
    if x_score == 3:
        print("Player one wins!")
    print(x_score)
                
                
            
    #raise NotImplementedError


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
    #takes board as input and return optimal move for the player on that board
    #the move returned should be optimal action (i,j)
    #if the board is in terminal board, minimax should return None
    raise NotImplementedError
