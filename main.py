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
print(r1)

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
    
    def __eq__(self, other):
        if self.name == other.name and self.birth_year == other.birth_year and self.email == other.email:
            return True
        else:
            return False
   
    def __repr__(self):
        return self.name + ' was born in ' + str(birth_year) + ' years old and his/her email is: ' + self.email

    # Write a method that calculates the age of this person 
    def calc_age(self):
        return current_year - self.birth_year

p1 = Person('Alice', 'alice@example.com', 2001)
p2 = Person('Bob', 'bob@example.com', 1999)
p3 = Person('Alice', 'alice@example', 2001)
p4 = Person('Charlie', 'bob@example.com', 1999)

# Work on the below for homework. 
# Try to be creative about the way that you do things! Use lists, use new variables, use dictionaries! 

# Write a function that identifies duplicates
def duplicates(e1, e2, e3, e4):
    inputs = [e1, e2, e3, e4]
    dupe = []
    for i in range(len(inputs)):
        for j in range (i+1, len(inputs)):
            for k in range(3):
                if input[i][]
# Write a function will categorize the people in order of age 
def order_of_age(e1, e2, e3, e4):
    inputs = [e1,e2,e3,e4]
    for i in range(len(inputs)):
        for j in range(len(inputs) - 1):
            if 
# Write a function that will identify if the name of the person is different, but the email address is the same. 


