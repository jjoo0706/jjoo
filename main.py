# The goal: Code Connect 4 
# Steps: 
# Being able to represent Connect 4 
# Being able to input x and o 
# Need a way to identify a win

' __init__: for self.rows, self.columns, self.grid
'display: going to display the board
'drop_piece: going to drop a piece in a certain coordinate (also going to see if a row is full or not)
'ex) (1,4)
'full: going to see if the board is full or not
'identify_win'

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
    def diplay(self):
        row = 0
        while row < self.rows:
            line = '|'
            column = 0
            while column < self.columns:
                line += self.grid[row][column] + '|'
                column += 1
            print(line)
            r += 1
        
    def drop_piece(self, row, col, piece):
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

    def identify_win(self, piece):
        r = 0
        while r < self.rows:
            c = 0
            while c < self.columns - 3:
                if self.grid[r][c] == piece and self.grid[r][c+1] == piece and self.grid[r][c+2] == piece and self.grid[r][c+3] == piece:
                    return True
                c += 1
            r += 1
        c = 0
        while c < self.columns:
            r = 0
            while r < self.rows - 3:
                if self.grid[r][c] == piece and self.grid[r+1][c] == piece and self.grid[r+2][c] == piece and self.grid[r+3][c] == piece:
                    return True
                r += 1
            c += 1

        r = 0
        while r < self.rows - 3:
            c = 0
            while c < self.columns - 3:
                if self.grid[r][c] == piece and self.grid[r+1][c+1] == piece and self.grid[r+2][c+2] == piece and self.grid[r+3][c+3] == piece:
                    return True
                c += 1
            r += 1
        r = 0
        while r < self.rows:
            c = 0
            while c < self.columns - 3:
                if self.grid[r][c] == piece and self.grid[r-1][c+1] == piece and self.grid[r-2][c+2] == piece and self.grid[r-3][c+3] == piece:
                    return True
                c += 1
            r += 1
        return False