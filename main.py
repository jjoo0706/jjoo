students = [['Alice', 90], ['Bob', 87], ['Charlie', 92], ['David', 84], ['Eric', 95], ['Frank', 80]]

# First, create a dictionary of the students' names and grades 

def student_dict():
	student = {}
	for i in students:
		name = i[0]
		grade = i[1]
		student[name] = grade
	return student

sd = student_dict() 

# Create a function that takes in a student's name and asks for input for the updated grade
# If the student hasn't been added to the dictionary yet, make sure the function can add them and their grade to the dictionary  

def grade_update(x, name):
	if name in x:
		new_grade = int(input("Enter the new grade: "))
		x[name] = new_grade
		print("Grade updated. The student's grade is now " + str(new_grade))
	else:
		new_grade = int(input("That student is not in the gradebook. Enter their grade to add them: "))
		x[name] = new_grade
		print("Student added!. The student's grade is now " + str(new_grade))
	
# print(sd)
# print(grade_update(sd, 'Daniel'))
# print(sd)

# Write a function that counts the number of occurrences of each word in a string. 

text = "apple banana apple orange banana apple orange orange"

def word(x):
	counter = {}
	word = ""
	for i in x:
		if i != " ":
			word += i
		else:
			if word in counter:
				counter[word] += 1
			else:
				counter[word] = 1
			word = ""
	if word in counter:
		counter[word] += 1
	else:
		counter[word] = 1
	return counter


f = open('sample.txt', 'r')
# print(f.read())

# Using this, keep a counter of the frequency of words. 
for line in f: 
	print(line)

def word_frequency():
	f = open('sample.txt', 'r')
	counter = {}
	word = ""
	for i in f:
		for j in i:
			if j != " " and j != "\n":
				word += j
			else:
				if word in counter:
					counter[word] += 1
				else:
					counter[word] = 1
				word = ""
	if word in counter:
		counter[word] += 1
	else:
		counter[word] = 1
	return counter

# print(word_frequency())

# ASSIGNED 2/22/25
# Write a function that will use the information in hw1.txt to interact with the user. 
# The function will first ask the user to input the information they want (Age, Email). 
# Then the function will ask for the name. 
# If the name does not exist in the file, the code will ask if they want to add a new person to the file. 
# When the user is done and the code quits, the function will print out all the information that was stored. 

# Continued 3/1 
# Add a option for the user to add a new name, new age, and new email 
# After the user is done, write the NEW dictionary to a NEW file. 

def hw1():
	filename = 'hw1.txt'
	new_filename = 'new_hw1.txt'
	data = {}
	x = open(filename, 'r')
	for i in x:
		name = ""
		age = ""
		email = ""
		counter = 0
		for j in i:
			if j == ",":
				counter += 1
			elif counter == 0:
				name += j
			elif counter == 1:
				age += j
			elif counter == 2 and j != "\n":
				email += j
		data[name] = (age, email)
	while True:
		info = input("Get 'Age', 'Email', or 'Add' new person? Type 'quit' to exit: ")
		if info == "quit":
			break
		if info == "Add":
			new_name = input("Enter new name: ")
			new_age = input("Enter new age: ")
			new_email = input("Enter new email: ")
			data[new_name] = (new_age, new_email)
		else:
			name = input("Enter name: ")
			if name in data:
				if info == "Age":
					print(name + "'s Age: " + data[name][0])
				else:
					print(name + "'s Email: " + data[name][1])
			else:
				print(name + " not found.")	
	new_file = open(new_filename, 'w')
	# Write all the info in one line, separated by a commma, and then for a new person, write a new line using the '\n'
	for name in data:
		new_file.write(name + "," + data[name][0] + "," + data[name][1] + "\n")
	new_file.close()
	print(data)
	x.close() 

print(hw1())