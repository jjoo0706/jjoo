# For homework, let's continue to work on writing the permutations for strings of length 2! Then we can extend to strings of length 3. Remember, we're focusing on writing this function with loops! 
# List of tools that might be helpful: 
#   Nested loops (for loops within for loops)
# def nested_loop_example(x): 
#     for i in x: 
#         for j in x: 
#             print(i, j)

# print(nested_loop_example([1,2,3]))

# String slicing 

# Focus on getting the funciton for string length of 2 to works. 
# If you don't get to string length of 3, that's okay. 

# def factorial(n): 
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(3))


# Write a function in recursion that sorts a list of integers.
# [3, 8, 6, 1] -> [1, 3, 6, 8]

# def ListInt(x):

# Write a function that will generate all permutations of a string using recursion.
# 'abc' -> ['abc', 'acb', 'bca', 'bac', 'cab', 'cba']
# There's obviously a way to do this with loops, and there's also a way to do this with recursion. 

# Write the function that will do the above with loops. 
    
# def s(x):
#     lst = [x]
#     for i in x:
#         if i + x[1] in lst:
#             lst = lst
#         elif i and x[1] in lst:

def PermutationsStr(x):
    permutations = []
    for i in range(len(x)):
        for j in range(len(x)):
            if i != j:
                permutations += [x[i] + x[j]]
    return permutations
# print(PermutationsStr('ab'))

def Permutations3(x):
    permutations = []
    for i in x:
        for j in range(len(x)):
            for k in range(len(x)):
                if i != j and i != k and j != k:
                    permutations += [x[i] + x[j] + x[k]]
    return permutations
# print(Permutations3('abc'))


# Homework assigned 10/27 
# Work on the below code to the best of your ability 

def remove_letter(x, y):
    NewWord = ''
    for i in x:
        if i != y:
            NewWord += i
    return NewWord

# Assigned 11/10 
# Write a function that will write down the permutations of the string using the below logic. 
# ['a']
# ['ba', 'ab']
# ['cab', 'acb', 'abc'] + ['cba', 'bca', 'bac']
# ['cab', 'acb', 'abc', 'cba', 'bca', 'bac']

def Permutations3_v2(x): 
    permutations = []
    Comb = ''
    for i in x:
        if i in x:
            Comb = remove_letter(x, i)
            permutations += [i + Comb]
            permutations += [i + Comb[1] + Comb[0]]
    return permutations

# print(Permutations3_v2('abc'))

# def Permutations3_v3(x):
#     permutations = []

p = ['a']
# Write code that will add the 'b' to the different positions 
# ['ba', 'ab']

def PosB(x):
    # print("p", p)
    lst = []
    lst += [x + p[0]]
    lst += [p[0] + x]
    return lst
# print(PosB('b'))

p1 = ['ba', 'ab']
# ['cba', 'bca', 'bac', 'cab', 'acb', 'abc']

def Comb(x, y):
    lst = []
    for i in x:
        lst += [y + i]
        lst += [i[0] + y + i[1]]
        lst += [i + y]
    return lst
# print(Comb(p1, "c"))

# ASSIGNED 12/8: work on this code so that it works for lists of any size with any permutation. 
# x : list of any size that are permutations 
# y : a character 
# goal: function that will input the new character into every position of every permutation in the list x  
def Comb1(x, y):
    lst = []
    for i in x:
        for i in range(len(i) + 1):
            lst += x[:i] + [y] + x[i:]
    return lst 
print(Comb1(['a'], 'b'))
print(Comb1(['ab', 'ba'], "c"))
print(Comb1(['cab', 'acb', 'abc', 'cba', 'bca', 'bac'], 'd'))

def original_comb1(x,y):
    lst = [] 
    for num in range(2): 
        print("num", num)
        for i in range(len(x) + 1):
            print("i", i)
            print("x", x)
            print("x[num]", x[num])
            print("x[num][:i]", x[num][:i])
            print("y", y) 
            print("x[num][i:]", x[num][i:])
            lst += [x[num][:i] + y + x[num][i:]]
            print("lst", lst)
    return lst

print(original_comb1(['ab', 'ba'], "c"))