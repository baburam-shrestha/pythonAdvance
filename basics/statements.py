# An instructions that a Python interpreter can execute are called statements
#  assignment statement, if statement, for statement, while statement


# Multi-line statement the end of a statement is marked by a newline character
# But we can make a statement extend over multiple lines with the line continuation character (\)

a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print(a)

# This is an explicit line continuation.
# line continuation is implied inside parentheses ( ), brackets [ ], and braces { }
a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)
print(a)
colors = ['red',
          'blue',
          'green']

print(colors)
a = 1; b = 2; c = 3 # multi assignment in a line
