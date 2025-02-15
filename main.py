a = ['Alice', 'red', 'apple'] 
b = ['Bob', 'blue', 'banana'] 
c = ['Charlie', 'blue', 'apple'] 
d = ['David', 'blue', 'pear']

# # There is 1 red. 
# # There is 3 blue. 
# # There are 2 apple.
# # There is 1 banana. 
# # There is 1 pear.  

# def counter(x):
# 	# The list will always be in the same order: name, color, fruit. 
# 	counternumF = 0
# 	counternumC = 0
# 	fruit_counter = []
# 	color_counter = []
# 	fruits = ["apple", "banana", "pear"]
# 	color = ["red", "blue"]
# 	for i in x:
# 		for x in i[1:]:
# 			if x in fruits:
# 				if x in fruit_counter:
# 					counternumF += 1
# 				else:
# 					fruit_counter = [x]
# 					counternumF = 1
# 			elif x in color:
# 				if x in color_counter:
# 					counternumC += 1
# 				else:
# 					color_counter = [x]
# 					counternumC = 1
# 	for fruits in fruit_counter:
# 		print(fruits, counternumF)
# 	for color in color_counter:
# 		print(color, counternumC)
# data = [a, b, c, d]
# print(counter(data))

# d = {'apple': [1,2,3]}
# print(d['apple'])
# d['apple'] = 3 
# print(d['apple'])

fruit = {} 
color = {} 
for l in [a, b, c, d]: 
	for ind in range(len(l)): 
		if ind == 1: 
			current_color = l[ind]
			if current_color in color: 
				color[current_color] += 1 
			else: 
				color[current_color] = 1 
		elif ind == 2: 
			current_fruit = l[ind]
			if current_fruit in fruit: 
				fruit[current_fruit] += 1 
			else: 
				fruit[current_fruit] = 1 
print(fruit)
print(color)

for i in fruit: 
	print("There are", fruit[i], i)
for i in color: 
	print("There are", color[i], i)

# I'll write up a more detailed description of dictionaries. 
# Based off of the write up, I want you to try to do some easy exercises on dictionaries, which I'll include as homework. 