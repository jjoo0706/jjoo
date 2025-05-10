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
print(freqs["romeo"])
# print out how many times "love" is in the text 
print(freqs["love"])
# print out how many distinct words are in the text 
print(len(freqs))

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
            else:
                if word != '':
                    words += [word.lower()]
                    word = ''
        if word != '':
            words += [word.lower()]
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

print(next_word('sample.txt'))