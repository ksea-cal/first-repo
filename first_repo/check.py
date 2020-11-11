def vertical_check(board):
    first_column = board[(0, 0)] == board[(0, 1)] and board[(0, 1)] == board[(0, 2)] and board[(0, 0)] != ' '
    second_column = board[(1, 0)] == board[(1, 1)] and board[(1, 1)] == board[(1, 2)] and board[(1, 0)] != ' '
    third_column = board[(2, 0)] == board[(2, 1)] and board[(2, 1)] == board[(2, 2)] and board[(2, 0)] != ' '
    return first_column or second_column or third_column

def horizontal_check(board):
    if (board[(0, 0)] == board[(1, 0)] and  board[(1, 0)] == board[(2, 0)] and board[(0, 0)] != ' '):
        return True
    elif (board[(0, 1)] == board[(1, 1)] and  board[(1, 1)] == board[(2, 1)] and board[(0, 1)] != ' '):
        return True
    elif (board[(0, 2)] == board[(1, 2)] and  board[(1, 2)] == board[(2, 2)] and board[(0, 2)] != ' '):
        return True
    else:
        return False


def diagonal_check(board):
    if board[(0, 0)] == board[(1, 1)] and board[(1, 1)] == board[(2, 2)] and board[(0, 0)] != ' ':
        return True
    elif board[(0, 2)] == board[(1, 1)] and board[(1, 1)] == board[(2, 0)] and board[(0, 2)] != ' ':
        return True
    else:
        return False


def draw_check(board):
    vertical = vertical_check(board)
    horizontal = horizontal_check(board)
    diagonal = diagonal_check(board)

    return not vertical or not horizontal or not diagonal
