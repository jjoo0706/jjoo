import random

# Write a function that simulates a coin flip. 
def coin_flip():
    num = random.randint(0, 1)
    if num == 0:
        return("Heads")
    else:
        return("Tails")
# print(coin_flip())

# Write a function that generates a random password. 
# random.choice() - look up how it works! 
# https://docs.python.org/3/library/random.html

def generate_password(x):
    low = 'qwertyuiopasdfghjklzxcvbnm'
    up = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    num = '124567890'
    punc = '!@#$%^&*()-=_+[]\{}|;:,./<>?'
    characters  = low + up + num + punc
    password = ''
    for i in range(x):
        password += random.choice(characters)   
    return password

# print(generate_password(16))

# Write a function that picks 6 unique random numbers from 1-50. 
def rand_num():
    nums = []
    while len(nums) < 6:
        num = random.randint(1, 50)
        if num in nums:
            nums = nums
        else:
            nums += [num]
    return nums
# print(rand_num())

# Represent a deck of cards 

# Deal a random set of cards 

def print_cards():
    classes = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    nums = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = []
    for i in classes:
        for j in nums:
            card = (j, i)
            deck += [(card)]
    # num = random.randint(1, 52)
    return deck
    
cards = print_cards() 

def deal_cards(x):
    set = []
    while len(set) < x:
        num = random.randint(1, 52)
        if cards[num] in set:
            set = set
        else:
            set += [cards[num]]
    return set

print(deal_cards(5))

# ASSIGNED MAY 27 
# Deal multiple sets of cards. Specify number of cards to deal and the number of people that need a set of cards. 
def deal(player, card):
    used = [0] * 52
    players = {}
    p = 1
    while p <= player:
        i = 0
        while i < card:
            c = random.randint(0,51)
            if used[c] == 0:

        

# Write a scoring function for the cards. 
def score(card):
    rank = card[0]
    if rank == 'Jack':
        return 11
    if rank == 'Queen':
        return 12
    if rank == 'King':
        return 13
    if rank == 'Ace':
        return 14
    return int(rank)

# Write a function that picks a random player and picks a random card from that player, and calculates the score of that card. 

