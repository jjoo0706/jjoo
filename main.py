import random

# Refresher on Dictionaries 
# {key: value}
x = {"Jayden": "Python", "Julie": "Java"}
# print(x["Jayden"])
# print(x["Julie"])

list_colors = ["red", "red", "blue", "green", "blue", "green", "red", "green"]
# Using a dictionary, count the number of instances of each color. 

def color_counter():
    counter = {}
    for color in list_colors:
        if color in counter:
            counter[color] += 1
        else:
            counter[color] = 1
    return counter
# print(color_counter())

# Write a function that reads a file and counts the instances of each word. 

# include case sensitivity 
def word_counter(filename):
    counter = {}
    file = open(filename, 'r')
    for i in file:
        word = ''
        for j in i:
            if (65 <= ord(j) <= 90) or (97 <= ord(j) <= 122) or ord(j) == 39: 
                word += j
            else:
                if word != '':
                    word1 = word.lower()
                    if word1 in counter:
                        counter[word1] += 1
                    else:
                        counter[word1] = 1
                    word = ''
        if word != '':
            word1 = word.lower()
            if word1 in counter:
                counter[word1] += 1
            else:
                counter[word1] = 1
            word = ''
    file.close()
    return counter

freqs = (word_counter('romeoandjuliet.txt'))
#print out how many times "Romeo" is in the text 
# print(freqs["romeo"])
# print out how many times "love" is in the text 
# print(freqs["love"])
# print out how many distinct words are in the text 
# print(len(freqs))

# END GOAL: Write a function that will generate new text! Markov Chain 

# ASSIGNED MAY 13 
# Write a function that keeps track of the next word in a sentence. The key will be the first word, and the value will be the second word. If the word is in the beginning of the sentence, the key will be $. 
# {"$": ["Python"], "Python": ["is"]}... 
# test it on sample.txt 
# Keep capitalized words! 

def next_word(filename):
    counter = {}
    file = open(filename, 'r')
    for i in file:
        word = ''
        words = []
        for j in i:
            if (65 <= ord(j) <= 90) or (97 <= ord(j) <= 122) or ord(j) == 39: 
                word += j
            elif ord(j) == 46:
                word += '.'
            else:
                if word != '':
                    words += [word]
                    word = ''
        if word != '':
            words += [word]
        if len(words) > 0:
            first_word = words[0]
            if '$' in counter:
                counter['$'] += [first_word]
            else:
                counter['$'] = [first_word]
            i = 0
            while i < len(words) - 1:
                k = words[i]
                v = words [i + 1]
                if k in counter:
                    counter[k] += [v]
                else:
                    counter[k] = [v]
                i += 1
    file.close()
    return counter

dct = (next_word('sample.txt'))
# print(dct)
# print(random.randint(0,1))

# Write a function that will generate a text. 
# Pick a random word that starts at the beginning of te sentence. 
# Then pick another random word that follows that word, etc. 
# How do you know when to end? 

# Instead of max_words, do max_sentences 
# we want it to look like a sentence -- so capitalize the first word and end the sentence in a period. 
def generate_text(dct, max_sentences):
    sentence = ''
    counter = 0
    while counter < max_sentences:
        start = dct['$']
        index = random.randrange(0, len(start))
        current = start[index]
        sentence += current
        while current in dct and current[-1] != '.':
            nxt = dct[current]
            index = random.randrange(0, len(nxt))
            current = nxt[index]
            sentence = sentence + ' ' + current
        sentence = sentence[0].upper() + sentence[1:]
        if sentence[-1] != '.':
            sentence = sentence + '. '
        counter += 1
    return sentence
print(generate_text(dct, 3))

# ASSIGNED MAY 17 
# We'll do some more practice with the random package and dictionaries. 
