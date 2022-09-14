
# who like this
# You probably know the "like" system from Facebook and other pages
# People can "like" blog posts, pictures or other items
# We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item
# It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

def likes(names):
    # your code here
    if len(names)==0:
        return 'no one likes this'
    elif len(names)==1:
        return names[0]+' likes this'
    elif len(names)==2:
        return names[0]+' and '+names[1]+' like this'
    elif len(names)==3:
        return names[0]+', '+names[1]+' and '+ names[2]+' like this'
    else:
        return names[0]+', '+names[1]+' and '+str(len(names)-2)+' others like this'


print(likes([]))
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))

def likes(names):
    formats = {
            0: "no one likes this",
            1: "{} likes this",
            2: "{} and {} like this",
            3: "{}, {} and {} like this",
            4: "{}, {} and {others} others like this"
        }
    n = len(names)
    return formats[min(n,4)].format(*names, others=n-2)


print(likes([]))
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))