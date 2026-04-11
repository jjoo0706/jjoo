# Linear Search 
# Write a function that will take in a list and a query and performs linear search

def linear_search(list, query):
    for i in range(len(list)):
        if list[i] == query:
            return "Number is in index " + str(i) + "."
    return "None"

numbers = [3, 1, 5, 7, 4, 9]
print(linear_search(numbers, 5))

# 1. Create a branch that is named binary-search 
# 2. Switch into that branch 
# 3. Push your files into binary-search branch