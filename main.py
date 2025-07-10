# The goal: Code Connect 4 
# Steps: 
# Being able to represent Connect 4 
# Being able to input x and o 
# Need a way to identify a win

# ' __init__: for self.rows, self.columns, self.grid
# 'display: going to display the board
# 'drop_piece: going to drop a piece in a certain coordinate (also going to see if a row is full or not)
# 'ex) (1,4)
# 'full: going to see if the board is full or not
# 'identify_win'

class Board: 
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.grid = []
        i = 0
        while i < self.rows:
            j = 0
            row = [' '] * self.columns
            self.grid += [row]
            i += 1
    def display(self):
        row = 0
        while row < self.rows:
            line = '|'
            column = 0
            while column < self.columns:
                line += self.grid[row][column] + '|'
                column += 1
            print(line)
            row += 1
        print(' 0 1 2 3 4 5 6')
    def drop_piece(self, col, piece):
        r = self.rows - 1
        while r >= 0:
            if self.grid[r][col] == ' ':
                self.grid[r][col] = piece
                return True
            r -= 1
        return False
    
    def full(self):
        r = 0
        while r < self.rows:
            c = 0
            while c < self.columns:
                if self.grid[r][c] == ' ':
                    return False
                c += 1
            r += 1
        return True

    # Is there a way to be more clever about this identify_win? 
    # At this point, we're checking the entire board every time we run identify_win 
    # Is there a way to make it so that we're not checking the entire board every single time? 
    # ASSIGNED JULY 2: try to think about a way to do this that prevents checking the entire board every single time 
    def identify_win(self, piece):
        # Check horizontal win 
        r = 0
        while r < self.rows:
            c = 0
            while c < self.columns - 3:
                if self.grid[r][c] == piece and self.grid[r][c+1] == piece and self.grid[r][c+2] == piece and self.grid[r][c+3] == piece:
                    return True
                c += 1
            r += 1
        # Check vertical win
        c = 0
        while c < self.columns:
            r = 0
            while r < self.rows - 3:
                if self.grid[r][c] == piece and self.grid[r+1][c] == piece and self.grid[r+2][c] == piece and self.grid[r+3][c] == piece:
                    return True
                r += 1
            c += 1
        # Check reverse diagonal (\) win
        r = 0
        while r < self.rows - 3:
            c = 0
            while c < self.columns - 3:
                if self.grid[r][c] == piece and self.grid[r+1][c+1] == piece and self.grid[r+2][c+2] == piece and self.grid[r+3][c+3] == piece:
                    return True
                c += 1
            r += 1
        # Check diagonal (/) win
        r = 0
        while r < self.rows:
            c = 0
            while c < self.columns - 3:
                if self.grid[r][c] == piece and self.grid[r-1][c+1] == piece and self.grid[r-2][c+2] == piece and self.grid[r-3][c+3] == piece:
                    return True
                c += 1
            r += 1
        
        return False

# Write a function that will start the Connect 4 Game using the Connect 4 object. 

def start_game():
    is_winner = False
    board = Board()
    piece = 'X'
    board.display()
    while not is_winner:
        if piece == 'X':
            print("Player " + piece + "'s turn")
            col_input = input("Choose a col from 0-6")
            if int(col_input) < 0 or int(col_input) > 6:
                print("Please choose from column 0-6")
                col_input = input("Choose a col from 0-6")
            else:
                col = int(col_input)
                if board.full() = True:
                    
                board.drop_piece(col, piece)
                board.display()
                if board.identify_win(piece) == True:
                    print("Player 1 wins!")
                    is_winner = True
                else:
                    piece = "O"
        elif piece == "O":
            print("Player " + piece + "'s turn")
            col_input = input("Choose a col from 0-6")
            if int(col_input) < 0 or int(col_input) > 6:
                print("Please choose from column 0-6")
                col_input = input("Choose a col from 0-6")
            else:
                col = int(col_input)
                board.drop_piece(col, piece)
                board.display()
            if board.identify_win(piece) == True:
                print("Player 2 wins!")
                is_winner = True
            else:
                piece = "X"
start_game()

# ASSIGNED JULY 2: play your own game a couple of times and see if there's any edge cases that don't work. Some examples include try hitting the edge of board; does it work as expected. Filling a column and trying to put down a piece; does it give you an error? The goal of this is to try to stress test your own code and identify if it runs as expected or if there's any errors. 
