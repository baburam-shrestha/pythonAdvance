# Decorators are a very powerful and useful tool in Python 
# since it allows programmers to modify the behaviour of a function or class
# Decorators allow us to wrap another function in order to extend the behaviour 
# of the wrapped function without permanently modifying it
# decorators are used to modify the behaviour of function or class
# functions are taken as the argument into another function and then called inside the wrapper function.

def fuse_decorator(decorators):
    def function_decorator(name):
        print(name,"works at Fusemachines Inc.")
        decorators(name)
    return function_decorator

@fuse_decorator
def babu_function(name):
    print(name)

name="Baburam Shresrtha"
babu_function(name)
    

#normal decorators
def decorators(functions):
    def inner_function():
        print("Inside the inner function")
        functions()
    return inner_function()

def functions():
    print("Inside the normal function")

decorators(functions)
# code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner
 
def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner
 
@decor1
@decor
def num():
    return 10
 
print(num())

#result with decorators chaining
def decorator_destinction_result(result_function):
    def destinction(marks):
        for mark in marks:
            if mark >= 80 and mark <100:
                print("DISTINCTION")
        result_function(marks)
    return destinction

def decorator_first_result(result_function):
    def first(marks):
        for mark in marks:
            if mark >=60 and mark <80:
                print("FIRST")
        result_function(marks)
    return first
def decorator_second_result(result_function):
    def second(marks):
        for mark in marks:
            if mark >=50 and mark <60:
                print("SECOND")
        result_function(marks)
    return second

def decorator_third_result(result_function):
    def third(marks):
        for mark in marks:
            if mark >=40 and mark <50:
                print("THIRD")
        result_function(marks)
    return third

@decorator_third_result
@decorator_second_result
@decorator_first_result
@decorator_destinction_result
def result(marks):
    for mark in marks:
        if mark>=35:
            pass
        else:
            print("FAIL")
            break
    else:
        print("PASS")

marks=[56,56,65,67,87,58,39,87]
result(marks)

