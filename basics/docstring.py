# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.

def square(n):
    '''Takes in a number n, returns the square of n''' 
    return n**2

# in this function, '''Takes in a number n, returns the square of n ''' is docstring 
# We can also use triple """ quotations to create docstrings and used for multiline comments

print(square.__doc__) # it print the docstring without quote