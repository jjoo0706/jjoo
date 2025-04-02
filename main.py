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

# Below are NOT functions, just lines of code 
# Construct 2 Rectangle objects 
r1 = Rectangle(80, 40)
r2 = Rectangle(60, 40)
# Print dimensions of each Rectangle object 
print(r1.width)
print(r1.height)
print(r2.width)
print(r2.height)
# Print area of each Rectangle object
print(r1.area())
print(r2.area())
# Grow both rectangles by 10 on each dimension 
r1.grow(10, 10)
r2.grow(10, 10)
# Print new dimensions
print(r1.width)
print(r1.height)
print(r2.width)
print(r2.height)

print("areas")
print(r1.area())
print(r2.area())
print(r1.area_val)

# ASSIGNED APR 1 
# Make a new class called Person 
# Add the following attributes: Name, Email, Age
# Make functions that will let you update their email and update their age