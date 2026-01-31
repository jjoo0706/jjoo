# Homework assigned on 1/31/26 

# QUESTION 1 
# Write a function that will detect a cycle. 
# https://www.geeksforgeeks.org/dsa/floyds-cycle-finding-algorithm/
# 1 -> 2 -> 3 -> 4 -----> false 
# 1 -> 2* - > 3 -> 4 -> 2* ------> true (4 points to 2*, which is the same 2* as the one between 1 and 3)

# QUESTION 2 
# Write a function that will reorder nodes so that: 
# 1. All the nodes < x will come before 
# 2. All the nodes >= x will come after
# 3. The order of the nodes is preserved 
# Example: 
# Input: 1 -> 4 -> 3 -> 2 -> 5 -> 1, x = 3
# Output: 1 -> 2 -> 1 -> 3 -> 4 -> 5  