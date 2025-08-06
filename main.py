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

import random

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
        self.piece_counts = {"X": 0, "O": 0}
        self.last_move = None
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
                self.piece_counts[piece] += 1
                # print("drop_piece, (r, col)", (r, col))
                self.last_move = (r, col)
                return True
            r -= 1
        return False
    
    def count_direction(self, row, col, piece, r_move, c_move):
        count = 0
        r = row + r_move
        c = col + c_move
        while 0 <= r < self.rows and 0 <= c < self.columns and self.grid[r][c] == piece:
            count += 1
            r += r_move
            c += c_move
        return count

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
    # When will there absolutely not be a win? 
    # when a spot is empty 
    # When there's been less than four moves, then there's definitely not going to be a win. 
    # Maybe do a point system? 
    # def identify_win(self, piece):
    #   Function that identifies win based on reading the entire board. 
    #     # Check horizontal win 
    #     r = 0
    #     while r < self.rows:
    #         c = 0
    #         while c < self.columns - 3:
    #             if self.grid[r][c] == piece and self.grid[r][c+1] == piece and self.grid[r][c+2] == piece and self.grid[r][c+3] == piece:
    #                 return True
    #             c += 1
    #         r += 1
    #     # Check vertical win
    #     c = 0
    #     while c < self.columns:
    #         r = 0
    #         while r < self.rows - 3:
    #             if self.grid[r][c] == piece and self.grid[r+1][c] == piece and self.grid[r+2][c] == piece and self.grid[r+3][c] == piece:
    #                 return True
    #             r += 1
    #         c += 1
    #     # Check reverse diagonal (\) win
    #     r = 0
    #     while r < self.rows - 3:
    #         c = 0
    #         while c < self.columns - 3:
    #             if self.grid[r][c] == piece and self.grid[r+1][c+1] == piece and self.grid[r+2][c+2] == piece and self.grid[r+3][c+3] == piece:
    #                 return True
    #             c += 1
    #         r += 1
    #     # Check diagonal (/) win
    #     r = 0
    #     while r < self.rows:
    #         c = 0
    #         while c < self.columns - 3:
    #             if self.grid[r][c] == piece and self.grid[r-1][c+1] == piece and self.grid[r-2][c+2] == piece and self.grid[r-3][c+3] == piece:
    #                 return True
    #             c += 1
    #         r += 1
        
    #     return False

    def identify_win1(self, piece):
        # Function that identifies if there is win by checking all directions of the current piece. 
        if self.piece_counts[piece] < 3 or self.last_move is None:
            return False
        row = self.last_move[0]
        col = self.last_move[1]
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        i = 0
        while i < len(directions):
            dr = directions[i][0]
            dc = directions[i][1]
            count = 1
            count += self.count_direction(row, col, piece, dr, dc)
            count += self.count_direction(row, col, piece, -dr, -dc)
            if count >= 4:
                return True
            i += 1
        return False


class Bot:
    def __init__(self, bot_piece, opp_piece, preferred_col, move_number):
        self.bot_piece = bot_piece
        self.opp_piece = opp_piece
        self.preferred_col = None
        self.move_number = move_number
    
    # Function that creates a deep copy of the current game board so that the bot can simulate moves.
    def copy_board(self, og_board):
        new_board = Board()
        new_grid = []
        for row in og_board.grid:
            new_row = []
            for c in row:
                new_row += [c]
            new_grid += [new_row]
        new_board.grid = new_grid
        new_piece = {}
        for i in og_board.piece_counts:
            new_piece[i] = og_board.piece_counts[i]
        new_board.piece_counts = new_piece
        new_board.rows = og_board.rows
        new_board.columns = og_board.columns
        new_board.last_move = og_board.last_move
        return new_board

    # Function that evaluates how good each column (0-6) is for the bot to play in.
    # If playing in the column lets the bot win immediately +1000
    # If the bot can block a column where the opponent could win +900
    # Small bonus points based on column position (Center = Best)
    def col_scores(self, board):
        scores = [0] * board.columns
        center = board.columns // 2

        c = 0
        while c < board.columns:
            col_score = 0
            if board.grid[0][c] != ' ':
                scores[c] = -10000
            else:
                temp_board = self.copy_board(board)
                temp_board.drop_piece(c, self.bot_piece)

                if temp_board.identify_win1(self.bot_piece):
                    col_score += 1000
                
                temp_board_opp = self.copy_board(board)
                temp_board_opp.drop_piece(c, self.opp_piece)

                if temp_board_opp.identify_win1(self.opp_piece):
                    col_score += 900
                
                if self.preferred_col == None:
                    pref = center
                else:
                    pref = self.preferred_col

                if pref >= c:
                    d = pref - c
                else:
                    d = c - pref
                
                if d == 0:
                    col_score += 3
                elif d == 1:
                    col_score += 2
                else:
                    col_score += 1

                if self.preferred_col != None:
                    if board.grid[0][self.preferred_col] == self.opp_piece:
                        if c == self.preferred_col:
                            col_score -= 100
                col_score += random.randint(0, 2)
                scores[c] = col_score
            c += 1
        return scores

    def choose_move(self, board):
        valid_col = []
        c = 0
        while c < board.columns:
            if board.grid[0][c] == ' ':
                valid_col += [c]
            c += 1

        if len(valid_col) == 0:
            return None

        if self.move_number == 0 or self.preferred_col is None:
            self.preferred_col = random.choice(valid_col)

        if self.preferred_col not in valid_col:
            self.preferred_col = random.choice(valid_col)

        scores = self.col_scores(board)


        max_score = -1
        s = 0
        while s < len(scores):
            if scores[s] > max_score:
                max_score = scores[s]
            s += 1

        best_col = []
        i = 0
        while i < len(scores):
            if scores[i] == max_score and board.grid[0][i] == ' ':
                best_col += [i]
            i += 1
            
        if len(best_col) > 0:
            move = random.choice(best_col)
        else:
            move = random.choice(valid_col)

        self.move_number += 1
        return move


# Write a function that will start the Connect 4 Game using the Connect 4 object. 

def start_game():
    is_winner = False
    board = Board()
    piece = 'X'
    board.display()
    
    mode = input("Enter 1 to play against another player. Enter 2 to play against a bot: ")
    if mode != "1" and mode != "2":
        print("Please choose 1 or 2.")
        mode = input("Enter 1 to play against another player. Enter 2 to play against a bot: ")
    if mode == "2":
        bot_player = Bot("O", "X", '', 0)

    while not is_winner:
        print("Piece counts", board.piece_counts)
        if piece == 'X':
            print("Player " + piece + "'s turn")
            col_input = input("Choose a column from 0-6")
            if int(col_input) < 0 or int(col_input) > 6:
                print("Please choose from column 0-6")
                col_input = input("Choose a col from 0-6")
            else:
                col = int(col_input)            
                position = board.drop_piece(col, piece)
                if position == False:
                    print("Column is full. Try a different one!")
                else:
                    board.display()
                    if board.identify_win1(piece) == True:
                        print("Player 1 wins!")
                        is_winner = True
                    else:
                        piece = "O"
        
        elif piece == "O":
            if mode == "1":
                print("Player " + piece + "'s turn")
                col_input = input("Choose a column from 0-6")
                if int(col_input) < 0 or int(col_input) > 6:
                    print("Please choose from column 0-6")
                    col_input = input("Choose a col from 0-6")
                else:
                    col = int(col_input)
            elif mode == "2":
                print("Bot's turn")
                col = bot_player.choose_move(board)
                print("Bot chooses column: " + str(col))
            position = board.drop_piece(col, piece)
            if position == False:
                print("Column is full. Try a different one!")
            else:
                board.display()
                if board.identify_win1(piece) == True:
                    print("Player 2 wins!")
                    is_winner = True
                else:
                    piece = "X"

        if board.full() and not is_winner:
            print("It is a tie! Restart to play again.")
start_game()

# ASSIGNED JULY 16 
# Try to implement a bot that you could play against! 
# We want to make our bot a little bit more intelligent. The way that we can do this is by giving a score to each of the columns. 
# Think of a scoring method that will help the bot decide which positions to pick. 
# Start writing a function that will have the bot keep track of these scores. 
# Remember you have to update the scores of the columns. 
# Make your own choice on deciding the scores of each of the columns. 
# NExt week: we'll talk about the way the bot will decide on which column. 

#JULY 23 
# Note: Remember to make notes and comments on your code pretty thoroughly. 
# Here, let's start thinking about where using classes would be helpful. Having a class object for a bot would be helpful since we can contain the methods within the class and we might want to call two bot objects to play against each other. 
# HW - Adjust your column deciding function. Add a littl bit of randomness to it. Use the random package in order to do this! 
# Try running Bot v Bot. This should not be deterministic. The patterns of the columns that they choose should be different. 

# JULY 30 
# Do iterative coding! Add one thing, test your function, and if it doesn't do what you want, add a new thing! 
# 1-2 hours on this. 
# Try Bot vs Bot -- only try it out! Write down some things you identified as not working as expected. 

# AUG 8 
# Given a list of scores, write code that will remove the unique values. 
# [3, 0, 1, 2, 0, 1, 1, 0] -> [3, 0, 1, 2]
# With this unique list, randomly pick a value. 
# [3, 0, 1, 2] -> 1 
# Then, make a list of the indices that this number appears in. 
# [2, 5, 6]
# Then pick randomly from this list! This will be the column you go down. 
# You can also code a different way to do it -- this is just one way to do it! 