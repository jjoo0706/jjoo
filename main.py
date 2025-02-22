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

print(word_frequency())