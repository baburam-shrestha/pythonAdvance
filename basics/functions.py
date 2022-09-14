# a function is a group of related statements that performs a specific task
# Functions help break our program into smaller and modular chunks.
# As our program grows larger and larger, functions make it more organized and manageable.
# it avoids repetition and makes the code reusable

# Syntax and example of Function


def greet(name):
    """
    This function greets to the person passed in as a parameter"""
    print("Hello, " + name + "\n Good morning!")
greet('baburam shrestha')

def get_area(l,b):
    length= l
    breath=b
    area= length*breath
    return area

print(f"Ares of Rectangle = {get_area(7,5)} square unit")

def function_result(marks):
    for mark in marks:
        if mark>=35:
            pass
        else:
            print("FAIL")
            break
    else:
        print("PASS")

marks=[56,56,45,67,87,58,39,87]
function_result(marks)