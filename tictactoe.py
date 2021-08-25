"""
Tic Tac Toe Player
"""
from random import randint

from copy import deepcopy

import math

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
    numX = 0
    numO = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                numX += 1
            elif board[i][j] == O:
                numO += 1
    
    if numX > numO:
        return O
    elif numO > numX:
        return X
    return X
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.append((i,j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    p = player(board)
    
    board2 = deepcopy(board)

    ac1 = action[0]
    ac2 = action[1]
    
    if board2[ac1][ac2] != EMPTY:
        raise Exception("This place isn't avaible")

    board2[ac1][ac2] = p
    return board2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """  

    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X" or board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return "X"
    
    for i in range(3):
        if board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X":
            return "X"

    for i in range(3):
        if board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
            return "X"

    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O" or board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return "O"
    
    for i in range(3):
        if board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O":
            return "O"
            
    for i in range(3):
        if board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
            return "O"
    
    return None
        

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    ganhador = winner(board) 

    if ganhador == "X":
        return 1
    elif ganhador == "O":
        return -1
    return 0


def max_value(state):
    v = -math.inf

    if terminal(state):
        return utility(state)

    for action in actions(state):
        v = max(v, min_value(result(state, action)))

    return v

def min_value(state):
    v = math.inf

    if terminal(state):
        return utility(state)

    for action in actions(state):
        v = min(v, max_value(result(state, action))) 

    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    teste1 = []

    if winner(board) != None:
        return None
    
    p = player(board)

    action = actions(board)
    
    if p == "X":
        if board == initial_state():
            return (randint(0,2), randint(0,2))
        v = -math.inf
        for acao in action:
            tmp = min_value(result(board, acao))
            if tmp > v:
                if tmp == 1:
                    return acao
                v = tmp
                board_return = acao
                
    else:
        v = math.inf
        for acao in action:
            tmp = max_value(result(board, acao))
            if tmp < v:
                if tmp == -1:
                    return acao
                v = tmp
                board_return = acao
                
    return board_return