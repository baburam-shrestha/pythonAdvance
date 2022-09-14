# Numbers 
integer_number=44
print(integer_number)
print(type(integer_number))
print(3+4)
print(3-4)
print(3*4)
print(3/4)
print(3//4)
print(3%4)
print(3**4)

print(2 + 3*4)
print((2 + 3) * 4) # The spacing has no effect on how Python evaluates

# Floats
# Python calls any number with a decimal point a float. This term is used in most programming languages, and 
# it refers to the fact that a decimal point can appear at any position in a number. 
# Every programming language must be carefully designed to properly manage decimal numbers
# so numbers behave appropriately no matter where the decimal point
float_number =3.44
print(float_number)
print(type(float_number))
print(3.44+4.55)
print(3.44-4.55)
print(3.44*4.55)
print(3.44/4.55)
print(3.44//4.55)
print(3.44%4.55)
print(3.44**4.55)

print(2.4 + 3.4*4.55)
print((2.3 + 3.23) * 4.422)

# Integers and Floats
print(4/2)

# If we mix an integer and a float in any other operation,we will get a float 
print(1 + 2.0)
print(2 * 3.0)
print(3.0 ** 2)

# Underscores in Numbers
# When we are writing long numbers, you can group digits using underscores to make large numbers more readable:
revenue = 14_000_000_000_999
print(revenue) # prints only the digits only
# Python ignores the underscores when storing these kinds of values. Even
# if you don’t group the digits in threes, the value will still be un­affected.

# Multiple Assignment
# we can assign values to more than one variable using just a single line.
x, y, z = 0, 0, 0
print(x,y,z)

# Constants
# A constant is like a variable whose value stays the same throughout the life of a program. 
# Python doesn’t have built-­in constant types, but Python pro grammers use all capital letters to 
# indicate a variable should be treated as a constant and never be changed:
PI_VALUES=22/7
print(PI_VALUES)
PI_VALUES=23
print(PI_VALUES)
PI_VALUES+=1
print(PI_VALUES)

#In reality, we don't use constants in Python. 
# Naming them in all capital letters is a convention to separate them from variables, 
# however, it does not actually prevent reassignment.