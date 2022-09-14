cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# checking for equality
food ='Rice'
print(food=="Rice")

# Ignoring Case When Checking for Equality

food ='Rice'
# print(food='rice') # cause error because case in word
print(food.lower()=='rice')

vegetable = 'mushrooms'
if vegetable!= 'anchovies':
    print("Hold the anchovies!")

# Numerical Comparisons

age =34
print(age)
print(age==34)
print(age!=35)
print(age<=35)
print(age>=35)

# Checking Multiple Conditions
my_age = 20
your_age=17
# Using and to Check Multiple Conditions
print(my_age<18 and your_age>18)
# Using or to Check Multiple Conditions
print(my_age<18 or your_age>18)


if my_age>18 and your_age>18:
    print("we can vote")
elif my_age>18 and your_age<18:
    print("I can vote")
elif my_age<18 and your_age>18:
    print("You can vote")
else:
    print("we cannot vote ")


# checking the value is list
banned_users = ['andrew', 'carolina', 'david','baburam']
# Checking Whether a Value Is in a List
user = 'baburam'
if user in banned_users:
    print(f"{user.title()}, You can not post a response.")

# Checking Whether a Value Is Not in a List
user='hari'
if user not in banned_users:
    print(f"{user.title()}, You can post a response.")


# Boolean Expressions
boolean_value = True
print(boolean_value)
game_active = True
print(game_active)
can_edit = False
print(can_edit)
print(game_active is can_edit)
print(game_active is not can_edit)


# if Statements
age =19
#     Simple if Statements
if age >18:
    print(f"you can vote. you are {age} years old.")
#     if-else Statements
age=17
if age >18:
    print(f"you can vote. you are {age} years old.")
else:
    print(f"you cannot vote. you are below 18 and you are {age} years old.")
#     The if-elif-else Chain
age=17

if age<5:
    print('your bus fare  is zero')

elif age>5 and age<15:
    print('your bus fare is Rs.5 per kilometer.')

else:
    print('your bus fare is Rs.7 per kilometer.')

#     Using Multiple elif Blocks
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

#     Omitting the else Block
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40

print(f"Your admission cost is ${price}.")

#     Testing Multiple Conditions
requested_topping = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_topping:
    print('Adding mushrooms')
if 'pepperoni' in requested_topping:
    print('Adding pepperoni')
if 'extra cheese' in requested_topping:
    print('Adding cheese')
print("Finished making your pizza!")

# Using if Statements with Lists

# Checking for Special Items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# Checking That a List Is Not Empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")