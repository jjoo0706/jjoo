# Bot picks the word 
# How might you want to visualize playing hangman? 

# Visualization
def start_game():
  hangman_stages = [
    """ 
      -----
      |   |
          |
          |
          |
          |
    ========
    """,
    """
      -----
      |   |
      O   |
          |
          |
          |
    ========
    """,
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    ========
    """,
    """
      -----
      |   |
      O   |
     \|   |
          |
          |
    ========
    """,
    """
      -----
      |   |
      O   |
     \|/  |
          |
          |
    ========
    """,
    """
      -----
      |   |
      O   |
     \|/  |
     /    |
          |
    ========
    """,
    """
      -----
      |   |
      O   |
     \|/  |
     / \  |
          |
    ========
    """
    
]
  # Word choice
  import random
  word_list = ["python", "computer", "programming", "tennis", "television", "bicycle", "school", "mathematics", "videogame"]
  chosen_word = random.choice(word_list)

  # Game setup
  display = ["_"] * len(chosen_word)
  lives = 6
  guessed_letters = []
  
  print("Welcome to Hangman!")
  print(hangman_stages[0])

  while lives > 0 and "_" in display:
    guess = input("Guess a letter: ")
    if guess in chosen_word:
        print("There is a " + guess + "!")
        if guess in guessed_letters:
          print("You already guessed that letter.")
          continue
        guessed_letters += [guess]
        for i in range(len(chosen_word)):
            letter = chosen_word[i]
            if letter == guess:
                display[i] = guess
    else:
        lives -= 1
        print("Wrong guess! You have " + str(lives) + " remaining.")
        print(hangman_stages[len(hangman_stages) - 1 -lives])
  
  if "_" not in display:
    print("Congratulations! You guessed the word!")
  else:
    print("Game Over! The word was: " + chosen_word)

print(start_game())



# How will you update the stages when you have words with different lengths and different unique letters? 
# Don't change number of stages in hangman, but try to space out your stages. 
# ASSIGNED 9/15 finish this for homework 
