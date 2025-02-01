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
    
# print(permutation_generation('abc'))

def permutation_recursive(x):
    if len(x) == 1:
        return [x]
    result = []
    for i in range(len(x)):
        character = x[i]
        remain_char = x[:i] + x[1+i:]
        permutations = permutation_recursive(remain_char)
        for j in permutations:
            result = result + [character + j]
    return result

# print(permutation_recursive('abc'))

# ASSIGNED JAN 25 
# fix option 0 
def display_menu():
    numbers = [45, 80, 10, 30, 27, 50, 5, 15]
    new_list = []
    while True:
        print("Choose an option from 0-7")
        print("0: Save a new list of numbers ")
        print("1: View the Current list ")
        print("2: View the first value ")
        print("3: View the Last value ")
        print("4: View the Average value")
        print("5: View every other value")
        print("6: Add a number to every value ")
        print("7: Quit ")
        option = (input("Input an option from 0-7"))
        if option == "0":
            new_list = []
            print("Enter numbers for the new list. Type 'done' when finished")
            while True:
                value = input("Enter a number (or 'done' to finish)")
                if value == 'done':
                    break
                new_list += [int(value)]
            print("New list saved! New list is: " + str(new_list))
            numbers = new_list
        elif option == "1":
            print("Current list: " + str(numbers))
        elif option == "2":
            print("First value: " + str(numbers[0]))
        elif option == "3":
            print("Last value: " +str(numbers[7]))
        elif option == "4":
            average = sum(numbers) / len(numbers)
            print("Average value: " + str(average))
        elif option == "5":
            print("Every other value: " + str(numbers[::2]))
        elif option == "6":
            value = input("Enter a number to add to each value in the list")
            value = int(value)
            new_numbers = []
            for x in numbers:
                new_numbers += [x + value]
            numbers = new_numbers
            print("Updated list: " + str(numbers))
        elif option == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from 0-7")

display_menu()


    # [45, 80, 10, 30, 27, 50, 5, 15]
    # "Asks me to input an option number "
    # 0-8 
    # 0 Save a new list of numbers 
    # 1 View the Current list 
    # 2 View the first value 
    # 3 View the Last value 
    # 4 View the Average value 
    # 5 View every other value 
    # 6 add some number to every value 
    # 7 Quit 

# Another code using the input function and also using nested loops 

# Write a function that takes in a list of lists. Iterate through both the list and the lists of lists, and if the types is a string, then add it to a string that will create a sentence. If it's an integer, add it to the sum. 
# [["hello", 10, 2], [15, "world"], ["today", "is", 53, "saturday"], [12, "!"]]
# output: "hello world today is saturday" 92 

def input(x):
    sentence = ""
    total_sum = 0
    for i in x:
        for j in i:
            if type(item) == str:
                sentence += " "
                sentence += j
            elif type(item) == int:
                total_sum += j
    return sentence, total_sum

x = []
num_lists = int(input("Enter the number of sublists: "))

for i in range(num_lists):
    sublist = []
    num_items = int(input("Enter the number of items in sublist: "))
    for j in range(num_items):
        num = input("Enter item in sublist: 

        