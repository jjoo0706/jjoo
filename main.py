# Using for loops, make a nested list that includes 3 values in the nested list of multiples of 3. 
# [[3, 6, 9], [12, 15, 18], [21, 24, 27]]

# for j in range(1, 4)
# Multiplier
# multiplier = j + (i-1) * 3

def Mult3():
    nested_list = []
    for i in range(1, 4):
        i_list = []
        for j in range(1, 4):
            mult = j + (i-1) * 3
            num = 3 * mult
            i_list += [num]
        nested_list += [i_list]
    return nested_list

print(Mult3())

# ASSIGNED 12/24/24 
# 