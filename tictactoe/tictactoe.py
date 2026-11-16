"""
Tic Tac Toe Player
"""

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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    if x_count > o_count:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                possible.add((i, j))
    return possible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception
    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result_winner = winner(board)
    if result_winner == X:
        return 1
    if result_winner == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    def max_value(state):
        if terminal(state):
            return utility(state)
        v = -math.inf
        for action in actions(state):
            v = max(v, min_value(result(state, action)))
        return v
    def min_value(state):
        if terminal(state):
            return utility(state)
        v = math.inf
        for action in actions(state):
            v = min(v, max_value(result(state, action)))
        return v
    if player(board) == X:
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
        return best_action
    best_value = math.inf
    best_action = None
    for action in actions(board):
        value = max_value(result(board, action))
        if value < best_value:
            best_value = value
            best_action = action
    return best_action
