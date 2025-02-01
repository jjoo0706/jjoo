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