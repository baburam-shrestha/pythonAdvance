# Python Objects and Classes
# Python is an object-oriented programming language. Unlike procedure-oriented programming, where the main emphasis is on functions, object-oriented programming stresses on objects.

# An object is simply a collection of data (variables) and methods (functions) that act on those data. Similarly, a class is a blueprint for that object.

# We can think of a class as a sketch (prototype) of a house. It contains all the details about the floors, doors, windows, etc. Based on these descriptions we build the house. House is the object.

# As many houses can be made from a house's blueprint, we can create many objects from a class. An object is also called an instance of a class and the process of creating this object is called instantiation.

# Defining a Class in Python
# Like function definitions begin with the def keyword in Python, class definitions begin with a class keyword.

# The first string inside the class is called docstring and has a brief description of the class. Although not mandatory, this is highly recommended.

# Here is a simple class definition.

class MyNewClass:
    '''This is a docstring. I have created a new class'''
    pass

# A class creates a new local namespace where all its attributes are defined. Attributes may be data or functions.

# There are also special attributes in it that begins with double underscores __. For example, __doc__ gives us the docstring of that class.

# As soon as we define a class, a new class object is created with the same name. This class object allows us to access the different attributes as well as to instantiate new objects of that class.

class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')

print(Person.age)

print(Person.greet)

print(Person.__doc__)

# Creating an Object in Python
# We saw that the class object could be used to access different attributes.

# It can also be used to create new object instances (instantiation) of that class. The procedure to create an object is similar to a function call.

# >>> harry = Person()
# This will create a new object instance named harry. We can access the attributes of objects using the object name prefix.

# Attributes may be data or method. Methods of an object are corresponding functions of that class.

# This means to say, since Person.greet is a function object (attribute of class), Person.greet will be a method object.

class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# create a new object of Person class
harry = Person()
harry.greet()