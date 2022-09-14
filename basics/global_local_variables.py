# Global Variables
# In Python, a variable declared outside of the function or in global scope is known as a global variable 
# This means that a global variable can be accessed inside or outside of the function.

x = "global"

def glo():
    print("x inside:", x)

print("x outside:", x)


# Local Variables
# A variable declared inside the function's body or in the local scope is known as a local variable.

def loc():
    y = "local"
    print("y inside:", y)

# print("y inside:", y) # it generates the error i.e. NameError: name 'y' is not defined

# Global and local variables
# Here, we will show how to use global variables and local variables in the same code.

x = "global "

def glo_loc():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

glo_loc()

# Example 5: Global variable and Local variable with same name
x = 5
def foo():
    x = 10
    print("local x:", x)
foo()
print("global x:", x)