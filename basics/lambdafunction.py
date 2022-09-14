# an lambda/anonymous function is a function that is defined without a name.

# While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.

# Hence, anonymous functions are also called lambda functions.
# Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned. Lambda functions can be used wherever function objects are required.

# Program to show the use of lambda functions
double = lambda x: x * 2
print(double(5))

# Use of Lambda Function in python
# We use lambda functions when we require a nameless function for a short period of time.

# In Python, we generally use it as an argument to a higher-order function 
# Lambda functions are used along with built-in functions like filter(), map()

# Example use with filter()
# The filter() function in Python takes in a function and a list as arguments.

# The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True.

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)

# Example use with map()
# The map() function in Python takes in a function and a list.
# The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item.

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)