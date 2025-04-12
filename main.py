# Let's say we want to build an object for rectangles. 

class Rectangle: 
    """
    a blueprint for objects that represent a rectangular shape 
    """
    # Add a constructor 
    def __init__(self, init_width, init_height):
        # this is the constructor 
        # used to create new objects 
        # specifies the attributes 
        self.width = init_width 
        self.height = init_height
        self.area_val = 0 

    def area(self):
        return self.width * self.height

    def grow(self, dwidth, dheight): 
        self.width += dwidth
        self.height += dheight 
    
    # Write a method that calculates the perimeter 
    def perimeter(self):
        return (self.width * 2) + (self.height * 2)

    # Write a method that will increase the scale of the dimensions by some input. 
    def scale(self, factor):
        self.width = factor*self.width
        self.height = factor*self.height

    # Write a method that will check equality 
    def __eq__(self, other): 
        if self.height == other.height and self.width == other.width: 
            return True 
        else: 
            return False 

    # Write a method that will define how the object is printed 
    def __repr__(self):
        return str(self.width) + ' x ' + str(self.height)


# Below are NOT functions, just lines of code 
# Construct 2 Rectangle objects 
r1 = Rectangle(80, 40)
r2 = Rectangle(80, 40)
# print(r1)

# ASSIGNED APR 1 
# Make a new class called Person 
# Add the following attributes: Name, Email, Age
# Make functions that will let you update their email and update their age

current_year = 2025

class Person:
    def __init__(self, name, email, birth_year):
        self.name = name
        self.email = email
        self.birth_year = birth_year
    
    def update_email(self, n_email):
        self.email = n_email
    
    # __eq__ is specific for defining the function == for a object. 
    def __eq__(self, other):
        if self.name == other.name and self.birth_year == other.birth_year and self.email == other.email:
            return True
        else:
            return False
   
    def __repr__(self):
        return str([self.name, self.email, self.birth_year])

    # Write a method that calculates the age of this person 
    def calc_age(self):
        return current_year - self.birth_year

p1 = Person('Alice', 'alice@example.com', 1997)
p2 = Person('Bob', 'bob@example.com', 1999)
p3 = Person('Alice', 'alice@example.com', 1997)
p4 = Person('Charlie', 'bob@example.com', 2000)
p5 = Person('Charlie', 'bob@example.com', 2000)
p6 = Person('Charlie', 'bob@example.com', 2000)

print(p1 == p2)
print(p1 == p3)
print(p1.calc_age())

# Work on the below for homework. 
# Try to be creative about the way that you do things! Use lists, use new variables, use dictionaries! 

# i = 'hello' == j ='hello' 
# for l in i: 
#   for k in j: 
#       if i != j: 
#           break 
# 'hello' = 'helle' 

# Write a function that identifies duplicates
def duplicates(i1, i2, i3, i4):
    inputs = [i1, i2, i3, i4]
    dupe = []
    for i in range(len(inputs)):
        for j in range (i+1, len(inputs)):
            if inputs[i].name == inputs[j].name:
                dupe = dupe +[(inputs[i].name)]
            if inputs[i].email == inputs[j].email:
                dupe = dupe +[(inputs[i].email)]
            if inputs[i].birth_year == inputs[j].birth_year:
                dupe = dupe +[(inputs[i].birth_year)]
    return dupe

# def duplicates1(i1, i2, i3, i4):
#     inputs = [i1, i2, i3, i4]
#     for i in range(len(inputs)):
#         for j in range (i+1, len(inputs)):
#             if __eq__(inputs[i], inputs[j]) == True:
#                 print("Duplicate found at " + i + " and " + j)

# print(duplicates1(p1, p2, p3, p4))

lp = [p1, p2, p3, p4, p5, p6]
def duplicates2(list_people):
    list_duplicates = []
    for i in range(len(lp)): 
        for j in range(i+1, len(lp)): 
            if lp[i] == lp[j]: 
                list_duplicates += [lp[i]]
    return list_duplicates 

ld = duplicates2(lp)
# print(ld)

# Write a function that, given the original list and the list of duplicates, will generate a new list with NO dupliates. 
def remove_dupes(lst_people, dupes):
    new_list = []
    for i in lst_people:
        if i in dupes and i in new_list:
            new_list = new_list
        elif i not in dupes or i not in new_list:
            new_list += [i]
    return new_list

# print(remove_dupes(lp, ld))

def remove_dupes2(lst_people):
    new_list = []
    for i in lst_people:
        if i not in new_list:
            new_list += [i]
    return new_list

lp = remove_dupes2(lp)
# print(remove_dupes2(lp))

# Write a function will categorize the people in order of age 
def order_of_age(lst_people):
    for i in range(len(lst_people)):
        for j in range(len(lst_people) - 1):
            if lst_people[j].calc_age() > lst_people[j+1].calc_age():
                temp = lst_people[j]
                lst_people[j] = lst_people[j+1]
                lst_people[j+1] = temp
    return lst_people

print(order_of_age(lp))

# ASSIGNED APRIL 12: FIX NAME CHECKER, AND DO MORE FUNCTIONS
# Write a function that will identify if the name of the person is different, but the email address is the same. 
def name_checker(lst_people):
    result = []
    for i in range(len(lst_people)):
        for j in range(i + 1, len(lst_people)):
            if lst_people[i].email == lst_people[j].email and lst_people[i].name != lst_people[j].name:
                result += [lst_people[i], lst_people[j]]
    return result
print(name_checker(lp))

# Write a function that will read info.txt and create Person objects if a Person object doesn't exist for this person. 
def read_people(filename):
    people = []
    file = open(filename, 'r')
    for i in file:
        info = i.split(',')
        name = info[0]
        email = info[1]
        birth_year = int(info[2])
        new_person = Person(name, email, birth_year)
        for person in people:
            if new_person != person:
                people += [new_person]
    file.close
    return people

# Create an object called Email, which has the attributes sender, receiver, date sent, and content. 
class Email:
    def __init__(self, sender, receiver, date_sent, content):
        self.sender = sender
        self.receiver = receiver
        self.date_sent = date_sent
        self.content = content
