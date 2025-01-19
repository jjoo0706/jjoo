# Using for loops, make a nested list that includes 3 values in the nested list of multiples of 3. 
# [[3, 6, 9], [12, 15, 18], [21, 24, 27]]

# for j in range(1, 4)
# Multiplier
# multiplier = j + (i-1) * 3

# Add inputs to it so that you can adjust the output based on multiplier how many to do. 
# 2, 2 
# [2, 4], [6, 8]
def Multiplier(x, y):
    nested_list = []
    for i in range(1, y+1):
        i_list = []
        for j in range(1, y+1):
            mult = j + (i-1) * x
            num = x * mult
            i_list += [num]
        nested_list += [i_list]
    return nested_list

# print(Multiplier(2,2))

# Given a list of integers, find the unique triples that add up to the sum 
# [1, 2, 3, 4, 5]
# 9
# (1, 3, 5), (2, 3, 4)
# x + y + z = 9 

def Triples(x, y):
    nums = y
    triples = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == x:
                    triples += [(nums[i], + nums[j], + nums[k])]
                else:
                    triples = triples
    return triples
# print(Triples(12, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Recursion 
def factorial(n): 
    if n == 1: 
        return 1 
    else: 
        return n * factorial(n-1) 

# n = 5 
# 5 * 4 * 3 * 2 *1 

def factorial_loop(n): 
    result = 1 
    for i in range(1, n+1): 
        result = result * i 
    return result 

# print(factorial(5))
# print(factorial_loop(5))

# Given a list of integers, add all the integers in the list using recursion. 
def recursive_sum(x):
    if len(x) == 1:
        return x[0]
    else:
        return x[0] + recursive_sum(x[1:])
print(recursive_sum([1, 2, 3, 4, 5]))

# ASSIGNED 1/19 
# Using the permutation code below as a guide, do a first attempt at doing this code in a recursive way. 
def permutation_generation(s): 
    perm_list = [s[0]] 
    for i in range(1, len(s)): 
        current_char = s[i] 
        updated_list = [] 
        for perm in perm_list: 
            for pos in range(len(perm)+1):
                updated_list += [perm[:pos] + current_char + perm[pos:]]
        perm_list = updated_list
    return perm_list
    
print(permutation_generation('abc'))