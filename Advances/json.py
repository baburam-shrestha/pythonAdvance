# JSON (JavaScript Object Notation) is a popular data format used for representing structured data. 
# It's common to transmit and receive data between a server and web application in JSON format.

p = '{"name": "Bob", "languages": ["Python", "Java"]}'
# It's also common to store a JSON object in a file.

# importing json module
import json
# Parse JSON in Python
# The json module makes it easy to parse JSON strings and files containing JSON object.

# Python JSON to dict
# You can parse a JSON string using json.loads() method. The method returns a dictionary.


person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print( person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])


# Python read JSON file
# You can use json.load() method to read a file containing JSON object.

{"name": "Bob", 
"languages": ["English", "French"]
}
with open('path_to_file/person.json', 'r') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print(data)


# Convert dict to JSON

person_dict = {'name': 'Bob',
'age': 12,
'children': None
}
person_json = json.dumps(person_dict)

# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)
