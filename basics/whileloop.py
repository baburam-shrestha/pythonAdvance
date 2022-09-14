# The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.

# We generally use this loop when we don't know the number of times to iterate beforehand.

# Syntax and example  of while Loop in Python

# In the while loop, test expression is checked first. The body of the loop is entered only if the test_expression evaluates to True. After one iteration, the test expression is checked again. This process continues until the test_expression evaluates to False.

# In Python, the body of the while loop is determined through indentation.

# The body starts with indentation and the first unindented line marks the end.

# Python interprets any non-zero value as True. None and 0 are interpreted as False.


n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)

#while loop with else
# same as with for loops, while loops can also have an optional else block.

# The else part is executed if the condition in the while loop evaluates to False.

# The while loop can be terminated with a break statement. In such cases, the else part is ignored. Hence, a while loop's else part runs if no break occurs and the condition is false.


counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")