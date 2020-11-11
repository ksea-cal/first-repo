def change_player(player):
    return 1 - player

def number_to_coord(number):
    if number > 9:
        print("Invalid number")
        return

    horizontal = (number - 1) % 3
    vertical = (number - 1) // 3
    return (horizontal, vertical)

def play(board, player):
    if player == 0:
        player_piece = 'X'
    else:
        player_piece = 'O'

    move = int(input("Name me your move!"))

    coord = number_to_coord(move)

    board[coord] = player_piece
