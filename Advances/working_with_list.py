# Looping Through an Entire List
cars = ['bmw', 'audi', 'toyota', 'subaru','tata']
print(cars)
for car in cars:
    print(car.title())

magicians = ['alice', 'david', 'carolina']
print(magicians)
for magician in magicians:
    print(magician)

# Doing More Work Within a for Loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, create a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")   
# Doing More Work Within a for Loop
print("Thank you, everyone.\nFor a  great magic show!")


# Making Numerical Lists
number_list =[]
print(number_list)
print(type(number_list))
# Using the range() Function  
# printing the natural number   
for number in range(0, 10,1):
    print(number)

# printing the even number   
for number in range(0, 10,2):
    print(number)

# printing the odd number   
for number in range(1, 10,2):
    print(number)
# square number
for number in range(1, 10):
    print(number**2)

# cube number
for number in range(1, 10):
    print(number**3)

# Using range() to Make a List of Numbers
#natural numbers
numbers = list(range(0, 10))
print(numbers)

# even number 
numbers_even = list(range(0, 10,2))
print(numbers_even)

# odd number 
numbers_odd = list(range(1, 10,2))
print(numbers_odd)
#square number
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

#but
squares = [number**2 for number in range(1, 11)]
print(squares)

#cube number
cubes =[number**3 for number in range(1,11)]
print(cubes)

print([number**3 for number in range(1,11)])
# Simple Statistics with a List of Numbers
digits=list(range(1,10))
print(digits)
print(f"max value={max(digits)}")
print(f"min value={min(digits)}")
print(f"sum ={sum(digits)}")

