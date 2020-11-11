from check import * 
from gui import * 
from utils import *

def main():
    board = {
        (0, 0) : ' ',
        (0, 1) : ' ',
        (0, 2) : ' ',
        (1, 0) : ' ',
        (1, 1) : ' ',
        (1, 2) : ' ',
        (2, 0) : ' ',
        (2, 1) : ' ',
        (2, 2) : ' '
    }

    step = 0
    player = 0

    game_init()

    while step < 9:
        player = change_player(player)
        play(board, player)
        game_print(board)

        diag_chk = diagonal_check(board)
        h_check = horizontal_check(board)
        v_check = vertical_check(board)

        if diag_chk or h_check or v_check:
            print("Win!")
            another_game = input("Another game? [y/n]")
            if another_game == "y":
                main()
            else:
                break

        if step == 8:
            d_chk = draw_check(board)
            if diag_chk or h_check or v_check:
                print("Win!")
            elif d_chk:
                print("Draw!")
            else:
                print("Lose!")
            another_game = input("Another game? [y/n]")
            if another_game == "y":
                main()
            else:
                break
        step += 1

if __name__ == "__main__":
    main()
