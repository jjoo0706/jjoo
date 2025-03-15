# Write a function that will take in a text file from the user. 
# Give the user the following options: 
# 1) Return the entire file 
# 2) Return the longest string in the file 
# 3) Create a new file 
# input()

# s = "Hello my name is Python"
# def longest_word(x):
# 	longest = ""
# 	word = ""
# 	for i in x:
# 		if i != " ":
# 			word += i
# 		else:
# 			if len(word) > len(longest):
# 				longest = word
# 			word = ""
# 	if len(word) > len(longest):
# 		longest = word
# 	else:
# 		longest = longest
# 	return longest

# def processfile():
# 	filename = input("Enter the filename: ")
# 	file = open(filename, 'r')
# 	fileInfo = file.read()
# 	file.close()
# 	print("Choose an option")
# 	print("#1. Return the entire file")
# 	print("#2. Return the longest string in the file")
# 	print("#3. Create a new file")
# 	option = input("Enter the option 1, 2, or 3: ")
# 	if option == '1':
# 		print(fileInfo)
# 	elif option == '2':
# 		print(longest_word(fileInfo))
# 	elif option == '3':
# 		new_filename = input("Enter the new filename: ")
# 		new_fileInfo = input("Enter information for the new file: ")
# 		new_file = open(new_filename, 'w')
# 		new_file.write(new_fileInfo)
# 		new_file.close()
# 		print("New file created.")
# 	else:
# 		print("Invalid choice, please try again.")

# print(processfile())

# 'w' will erase the entire file and write the thing you want 
# 'a' will Append to the existing file 
with open('file.txt', 'a') as f: 
	f.write("\nHello World")


