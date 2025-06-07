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
        for i in 
