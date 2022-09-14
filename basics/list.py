bicycles = ['Trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(type(bicycles))

# Accessing Elements in a List
print(bicycles[0])
print(bicycles[1].title())
print(bicycles[0].lower())
print(bicycles[1].upper())

# Index Positions Start at 0, Not 1
print(bicycles[1]) # it print the second value in the list
print(bicycles[0]) # it print the first value in the list

print(bicycles[-1]) # it print the last value in the list it means that the negative indexing id done from last and start with -1

# Using Individual Values from a List
message = f"My first bicycle was a {bicycles[2].title()}."
print(message)


# Changing, Adding, and Removing Elements

# Modifying Elements in a List
print('Modifying Elements in a List')
motorcycles = ['honda', 'yamaha', 'pulsur','rtr','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding Elements to a List
# Appending Elements to the End of a List
print('Appending Elements to the End of a List')
motorcycles.append('tata')
print(motorcycles)

# Inserting Elements into a List
print('Inserting Elements into a List')
motorcycles.insert(3, 'hyundai') # it shifts every other value in the list one position to the right
print(motorcycles)


bus_list= ['honda', 'yamaha', 'suzuki','maruti','bmw']

# Removing an Item Using the del Statement
print("Removing an Item Using the del Statement")
del bus_list[2]
print(bus_list)

# Removing an Item Using the pop() 
print("Removing an Item Using the pop() ")
popped_bus=bus_list.pop()
print(bus_list)
print(popped_bus)

# Popping Items from any Position in a List
print("Popping Items from any Position in a List")
print(bus_list)
popped_bus_index=bus_list.pop(1)
print(bus_list)
print(popped_bus_index)

# Removing an Item by Value
print("Removing an Item by Value")
print(bus_list)
popped_value = bus_list.remove("maruti") # it removes the value from the list and not assigned to the variable
print(bus_list)
print(popped_value)


# Organizing a List

car = ['bmw', 'audi', 'toyota', 'subaru','tata']
print(car)
# Sorting a List Permanently with the sort() Method
print("Sorting a List Permanently with the sort() Method")
car.sort()
print(car)

car.sort(reverse=True)
print(car)

# Sorting a List Temporarily with the sorted() Function
print("Sorting a List Temporarily with the sorted() Function")
car = ['bmw', 'audi', 'toyota', 'subaru','tata']
print(car)

print(sorted(car))
print(sorted(car,reverse=True))
print(car)

# Printing a List in Reverse Order
print("Printing a List in Reverse Order")
cars = ['bmw', 'audi', 'toyota', 'subaru','tata']
print(cars)
cars.reverse() # it reverse the list permanently
print(cars)

# Finding the Length of a List
print("Finding the Length of a List")
length = len(cars)
print(f"{length}")
# list indexing
mountains=["Mt. everest ", 'kanchanjanga','machhapuchre','dhaulagiri','annapurna']
print(mountain for mountain in mountains)
print(mountains)
print(mountains[0]) #print the first index value
print(mountains[-1]) #print the last index value
print(mountains[2]) #print the third index value
print(mountains[-2]) #print the second last index value


#index slicing

print(mountains[:]) # print all elements
print(mountains[:4]) # print  elements from 1st to 3rd
print(mountains[1:]) # print from 2nd to last
print(mountains[-4:]) #print  from 4th last to last
print(mountains[:-2]) # print first to 3rd lasts

# Looping Through a Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')