# Bot picks the word 
# How might you want to visualize playing hangman? 

# Visualization
hangman_stage = [
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

for i in hangman_stage:
    print(i)

# Word choice
import random
word_list = ["python", "computer", "programming", "tennis", "television", "bicycle", "school", "mathematics", "videogame"]
chosen_word = random.choice(word_list)

# Game setup
for i in chosen_word:
    display += "_"
    lives = 6
    guessed_letters = []
    
# Guess letter 
while lives > 0 and "_" in display:
    guess = input("Guess a letter: ")
    if guess in chosen_word:
        print("There is a " + guess + "!")
        for i in range(len(chosen_word)):
            letter = chosen_word[i]
            if letter == guess:
                display[i] = guess
    else:
        lives -= 1
        print(hangman_stages[len(hangman_stages) - 1 -lives])

# How will you update the stages when you have words with different lengths and different unique letters? 
# Don't change number of stages in hangman, but try to space out your stages. 
# ASSIGNED 9/15 finish this for homework 
