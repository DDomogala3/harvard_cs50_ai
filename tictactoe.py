"""
Tic Tac Toe Player
"""

import math
import count_board
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
    if count_board.count_board(board)[0] > count_board.count_board(board)[1] and count_board.count_board(board)[3] > 9:
        return O
    elif count_board.count_board(board)[0] < count_board.count_board(board)[1] and count_board.count_board(board)[3] > 9:
        return X
    elif count_board.count_board(board)[3] == 9:
        print("FULL")
    #returns which players turn it is
   # raise NotImplementedError
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #returns set of actions that can be taken on a board
    #each action should be reported as a tuple
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #if action is not valid, raise an  exception
    #original board should be left unmodified
    
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #if no winner, return None
    raise NotImplementedError


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
