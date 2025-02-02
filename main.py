# Given a 2-D list, rotate the matrix 

# table = [[7, 4, 1]
#          [5, 3, 2]
 #         [6, 9, 8]] 

# rotated = [[6, 5, 7]
#             [9, 3, 4]
#             [8, 2, 1]]

def rotate_matrix(x):
    rows = len(x)
    columns = len(x[0])
    rotate = [[0] * rows for i in range(columns)]
    for j in range(rows):
        for k in range(columns):
            rotate[k][rows - 1 - j] = x[j][k]
    return rotate

print(rotate_matrix([[7, 4, 1], [5, 3, 2], [6, 9, 8]]))

# ASSIGNED 2/1/25 
# Write a function that takes in a 2-D list, and sums up all the rows and then all the columns. The function will output two different integers at the end. 

# Given a 2-D list, find the maximum element using loops. (Do not use the max() function)

# Given a 2-D list, check if the matrix is symmetric. This means matrix[i][j] == matrix[j][i] 