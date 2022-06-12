import random

def print_board(board):
        print(f"{board[0]}{board[1]}{board[2]}")
        print(f"{board[3]}{board[4]}{board[5]}")
        print(f"{board[6]}{board[7]}{board[8]}")

def valid_move(board,move):
    return ( move >= 1 and move <= 9 and board[move-1] == "-")

def check_win(board):

    # Horizontal
    if(board[0] == board[1] == board[2] and board[0] != '-'): return True
    if(board[3] == board[4] == board[5] and board[3] != '-'): return True
    if(board[6] == board[7] == board[8] and board[6] != '-'): return True

    # Diagonal
    if(board[0] == board[4] == board[8] and board[0] != '-'): return True
    if(board[2] == board[4] == board[6] and board[2] != '-'): return True

    # Vertical
    if(board[0] == board[3] == board[6] and board[0] != '-'): return True
    if(board[1] == board[4] == board[7] and board[1] != '-'): return True
    if(board[2] == board[5] == board[8] and board[2] != '-'): return True

    return False

def play_move(board,cur_player):

    while (True):

        if (cur_player == "O") : move = random.randint(0,8)
        else                   : move = int(input(f"{cur_player} Move (0-9) : "))

        if valid_move(board,move):
            board[move-1] = cur_player
            break
        else :
            if (cur_player == "X"): print("Invalid Move")


if __name__ == "__main__":

    # assumed dimension 3
    board = ["-"]*9 # 3x3 board
    cur_player = "X"

    while(True):
        print_board(board)
        play_move(board,cur_player)

        # Check win / lose / tie
        if(check_win(board)):
            print_board(board)
            print(f"{cur_player} wins")
            break
        elif("-" not in board) :
            print_board(board)
            print("Tie")
            break

        # Switch Player
        if(cur_player == "X") : cur_player = "O"
        else                  : cur_player = "X"

