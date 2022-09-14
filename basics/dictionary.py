# A Simple Dictionary
dictionary={1:'One',2:"Two",3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Enght',9:'Nine'}
print(dictionary)
print(type(dictionary))

# Working with Dictionaries
for values  in dictionary:
    print(f"{values}")

key= dictionary.keys()
value = dictionary.values()
print(key)
print(value)

# Accessing Values in a Dictionary
print(dictionary[1]) # it takes key of the dictionary
dictionary[10]='Ten'
print(dictionary)

# Starting with an Empty Dictionary

roll_name={}
print(roll_name)
print(type(roll_name))
#adding the key value pair in empty dictionary
roll_name[1]='baburam'
print(roll_name)
roll_name[2]="hari"
print(roll_name)

# Modifying Values in a Dictionary
roll_name[2]="shaym"
print(roll_name)
roll_name[3]='ram'
print(roll_name)

# Removing Key-Value Pairs
del roll_name[1]
print(roll_name)

# A Dictionary of Similar Objects
favorite_programming_languages={
    'babura,':'JAva',
    'shyam':'Python',
    'ram':"CPP",
    'hari':'C',
}
language = favorite_programming_languages['ram'].title()
print(f"Ram's favorite Programming language is {language}.")

# Using get() to Access Values
# print(favorite_programming_languages['hira']) # it cauese error 
# but
print(favorite_programming_languages.get('hira',"No value for the this key")) # it provide the certain output when mistake key is assigned for the value

# Looping Through a Dictionary
personal={
    'username':'Shresthababu',
    'first_name':'Shrestha',
    'last_name':'baburam',
    'age':4,
    'city':'kathmandu',
}

# Looping Through All Key-Value Pairs
for key, value in personal.items():
    print(f"{key}:{value}")

# Looping Through All the Keys in a Dictionary
for key in personal.keys():
    print(f"{key}")

# Looping Through All the values in a Dictionary
for value in personal.values():
    print(f"{value}")

# Looping Through a Dictionary’s Keys in a Particular Order
languages={
    'babura,':'JAva',
    'shyam':'Python',
    'ram':"CPP",
    'hari':'C',
}
for name in sorted(languages.keys()):
    print(f"{name}, thank you for the poll.")
print(languages)
