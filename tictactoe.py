import math
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
    xCounter = 0
    oCounter = 0

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == X:
                xCounter += 1
            elif board[i][j] == O:
                oCounter += 1

    if xCounter > oCounter:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                possibleActions.add((i, j))

    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Create new board, without modifying the original board received as input
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
    # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False
    #return True if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None) else False # noqa E501


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    # Check how to handle exception when a non terminal board is received.


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                print(v, move, "aa")
                return v, move
    print(v, move, "bb")
    return v, move


def min_value(board):

    if terminal(board):
        return utility(board), None

    v = math.inf
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                print(v, move, "cc")
                return v, move
    print(v, move, "dd")
    return v, move


''''"""
Tic Tac Toe Player
"""
import copy
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


cnt = 0


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    cnt_x = 0
    cnt_o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                cnt_x += 1
            elif board[i][j] == "O":
                cnt_o += 1
    if cnt_x > cnt_o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    arr = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                arr.add((i, j))
    arr = sorted(arr)
    return arr


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    turn = player(board)
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = turn
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        return board[2][0]
    # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            arrr = []
            for action in actions(board):
                arrr.append([max_val(result(board, action)), action])
            print(arrr, "ma")
            arrr.sort(reverse=True)
            return arrr[0][1]
        else:
            arrr = []
            print(actions(board))
            for action in actions(board):
                arrr.append([min_val(result(board, action)), action])
            print(arrr, "mi")
            arrr.sort()
            return arrr[0][1]


def max_val(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    act = None
    for action in actions(board):
        v = max(v, min_val(result(board, action)))
    return v


def min_val(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    act = None
    for action in actions(board):
        v = min(v, max_val(result(board, action)))
    return v

'''
'''"""
Tic Tac Toe Player
"""
import copy
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


cnt = 0


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    cnt_x = 0
    cnt_o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                cnt_x += 1
            elif board[i][j] == "O":
                cnt_o += 1
    if cnt_x > cnt_o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    arr = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                arr.add((i, j))
    return arr


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    turn = player(board)
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = turn
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        return board[2][0]
    # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_poss(board)
            return move
        else:
            value, move = min_poss(board)
            return move


def max_poss(board):
    if terminal(board):
        return utility(board), None
    v = -math.inf
    move = None
    for action in actions(board):
        a, aa = min_poss(result(board, action))
        print(result(board, action), "max", action)
        if a > v:
            v = a
            move = action
            if v == 1:
                return v, move
    return v, move


def min_poss(board):
    if terminal(board):
        return utility(board), None
    v = math.inf
    move = None
    for action in actions(board):
        a, aa = max_poss(result(board, action))
        print(result(board,action), "min")
        if a < v:
            v = a
            move = action
            if v == -1:
                print(action)
                return v, move

    return v, move'''