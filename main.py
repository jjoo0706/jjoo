# list1 = [1,2,3] 
# list2 = list1 
# list1[1] = 1 
# print(list2)
# list2[2] = 1 
# print(list1)

def mystery5(x): 
	x = x* -1 
	return x 

def mystery6(l1, l2): 
	l1[0] = 0
	l2 = [1, 1]

# x = 7 
# vals = [7, 7] 
# mystery5(x) 
# mystery6(vals, vals) 
# print(x, vals) 

# grid1 = [[1,2], [3,4], [5,6], [7,8]]
# grid3 = grid1[:]
# grid3[1][1] = 9 
# print(grid1)

# ASSIGNED 2/8/25 
# Try to write a code that will deep copy a 2-D list. 
# This is possible to do with the tools that we learned in lesson. 
# Don't use built in tools that you might find online. 

def deep_copy(x):
	list = []
	for i in x:
		row = i[:]
		list += [row]
	return list

