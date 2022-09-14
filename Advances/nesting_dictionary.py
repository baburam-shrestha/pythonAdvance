# Nesting of dictionary

color_1 = {'color': 'green', 'points': 5}
color_2 = {'color': 'yellow', 'points': 10}
color_3 = {'color': 'red', 'points': 15}
color = [color_1,color_2, color_3]
for co in color:
    print(co)

#   A List in a Dictionary
food=['rice','dal','achar','salad']
fruit=['apple','banana','pinapple','gauva']
food_fruit={
    'food':food,
    'fruit':fruit,
    'beer':'mafiya',

}
print(food_fruit)
print(type(food_fruit))

# dictionary in dictionary
users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
for username, user_info in users.items():

    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
