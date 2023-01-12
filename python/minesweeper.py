# thought process {{{

# }}} DEF End : thought process
# create a board : n*m
    # populate board with mines : num_mines
# display board

# ask for dig location (x,y)
# check if location (x,y) is a mine
    # if true then game over
    # else keep digging until current (x,y) is adjacent to mine

# repeat 2 and 3 until there are no open slots on board that are not bombs

# if you reach here you win



import random

class Board:

    # constructor
    def __init__(self , width , height , bombs):
        self.width = width
        self.height = height
        self.bombs = bombs

    def generate_board(self):
        # rows  = cols = list();
        # board = list(list());
        # rows  = []*num_rows
        # cols  = [rows]*num_cols
        # board = [[]*self.width]*self.height;

        board = [[None for _ in range(self.width)] for _ in range(self.height)]
        #print(board)

        # plant mines
        planted = 0;
        while (planted <= self.bombs):
            #get (x,y) of bomb randomly
            x = random.randint(0 , self.width - 1);
            y = random.randint(0 , self.height - 1);

            if (board[x][y] == "*"): continue
            board[x][y] = "*";
            planted     = planted + 1;
            #print(f"Bomb at : ({x},{y})")
        #print(board)

        def evaluate_baord(self):
            # assign every cell a value based on how many adjacted bombs there are to it
            for i in range(self.width):
                for j in range(self.height):
                    if (self.board[i][j] == "*"): continue
                    self.board[i][j] = self.get_neighboring_bombs(i,j)

        def get_neighboring_bombs(self, row, col):
            num_bombs = 0;
            # top left  : i-1 , j-1
            # top mid   : i-1 , j
            # top right : i-1 , j+1
            # left      : i   , j-1
            # right     : i   , j+1
            # bot left  : i+1 , j-1
            # bot mid   : i+1 , j
            # bot right : i+1 , j+1

            for i in range(row-1, (row+1)+1):
                for j in range(col-1, (col+1)+1):
                    if (i == row and j == col ): continue
                    if (self.board[i][j] == "*"): num_bombs = num_bombs + 1

        def diplay_board(self):
            print(board)


if __name__ == "__main__":

    width = height = 3;
    bombs = 3;

    game_board = Board(width , height, bombs);
    game_board.generate_board()

