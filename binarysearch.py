# Linear Search 
# Write a function that will take in a list and a query and performs linear search

def linear_search(list, query):
    for i in range(len(list)):
        if list[i] == query:
            return "Number is in index " + str(i) + "."
    return "None"

numbers = [3, 1, 5, 7, 4, 9]
# print(linear_search(numbers, 5))

# 1. Create a branch that is named binary-search 
# 2. Switch into that branch 
# 3. Push your files into binary-search branch
# DONE 

# Binary search slides: https://www.cs.cmu.edu/~15122/handouts/slides/review/06-binsearch.pdf

# Let's start with the first round of binary search 

def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = lst[mid]
        if mid_value == target:
            return True
        elif target < mid_value:
            right = mid - 1
        else:
            left = mid + 1
    return False

nums = [1, 3, 4, 7, 8, 11, 15]
print(binary_search(nums, 7))

# Exercise 1: In a list of repeating items, find the first instance of the item. Return index of first instance. 
# [1,2,2,2,3], 2 -> 1 

def first(lst, target):
    left = 0
    right = len(lst) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            result = mid
            right = mid - 1
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

nums = [1, 3, 3, 4, 7, 8, 11, 15]
print(first(nums, 3))

# Exercise 2: In a list of repeating items, find the last instance of the item. Return index of last instance. 
# [1,2,2,2,3], 2 -> 3 

def last(lst, target):
    left = 0
    right = len(lst) -1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            result = mid
            left = mid + 1
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

print(last(nums, 3))

# Exercise 3: In a list of repeating items, count the number of instances that a query has. 
# [1,2,2,2,3], 2 -> 3 

def repeating_items(lst, target):
    first_occ = first(lst, target)
    if first_occ == -1:
        return 0
    last_occ = last(lst, target)
    return last_occ - first_occ + 1 

print(repeating_items(nums, 3))

# Given a number, find the index in which it should be inputted. 
# [1,3,5,6], 2 -> index 1 

def index_input(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

print(index_input(nums, 6))
