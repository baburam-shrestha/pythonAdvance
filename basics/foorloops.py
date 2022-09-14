# the for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects
# Iterating over a sequence is called traversal.
# Loop continues until we reach the last item in the sequence 
# The body of for loop is separated from the rest of the code using indentation.
# Syntax and example of for Loop

numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0
# iterate over the list
for number in numbers:
    sum = sum+number

print(f"The sum is, {sum}")
sum 

# The range() function
# We can generate a sequence of numbers using range() function. 
# range(10) will generate numbers from 0 to 9 (10 numbers).
print(range(10))
# We can also define the start, stop and step size as range(start, stop,step_size)
print(list(range(2, 20, 3)))
# The range object is "lazy" in a sense because it doesn't generate every number 
# that it "contains" when we create it

# This function does not store all the values in memory; it would be inefficient.
#  So it remembers the start, stop, step size and generates the next number on the go.

# To force this function to output all the items, we can use the function list().


print(list(range(2, 8)))
#foor loop with else

# A for loop can have an optional else block as well. The else part is executed if the items in the sequence used in for loop exhausts.

# The break keyword can be used to stop a for loop. In such cases, the else part is ignored.

digits = [0, 1, 5]

for digit in digits:
    print(digit)
else:
    print("No items left.")
# list indexing

mountains=["Mt. everest ", 'kanchanjanga','machhapuchre','dhaulagiri','annapurna']
print([mountain for mountain in mountains])

def maskify(cc):
    length=len(cc)
    new_cc=''
    if length<=4:
        return cc
    for i in range(length-4):
        new_cc+="#"
    return new_cc + cc[-4:]
print(maskify('SF$SDfgsd2eA'))