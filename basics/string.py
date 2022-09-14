# Strings

# A string is a series of characters. Anything inside quotes is considered
# a string in Python, and you can use single or double quotes around your
# strings like this:
# eg. "This is a string."
# eg. 'This is also a string.'

string_variable1 = "This is a string."
string_variable2='This is also a string.'
print(string_variable1)
print(string_variable2)

strv1='I told my friend, "Python is my favorite language!"'
print(strv1)
strv2="The language 'Python' is named after Monty Python, not the snake."
print(strv2)
strv3="One of Python's strengths is its diverse and supportive community."
print(strv3)

#Changing Case in a String with Methods
book_name= "muna madan"

# title() function is capitalize the first letter of each words
print(book_name.title())

# uppper() function is used to uppercase the whole text or string
print(book_name.upper())
# lower() function is used to lowercase the whole text or string
print(book_name.lower())

# Variables in Strings
name = "baburam"
surname = "shrestha"
full_name = f"{name} {surname}"
message = f"Hello, {full_name.title()}!"
print(message)
# variable in string  another method
full_name1 = "{} {}".format(name, surname)
message1 = f"Hello, {full_name1.title()}!"
print(message1)

#Adding Whitespace to Strings with Tabs or Newlines

language= "Python"
print(language)
print(f"{language}\n")
print("\t"+language)
print(f"\t{language}")

#Stripping Whitespace
# Stripping Whitespace rstrip() function is used to remove the white space in the text ( at the end) 
string_stripping= "Programming in Cpp   "
print(string_stripping)
print(len(string_stripping))
print(string_stripping.rstrip())
print(len(string_stripping.rstrip()))
# Stripping Whitespace lstrip() function is used to remove the white space in the text ( at the start ) 
string_stripping= "   Programming in C"
print(string_stripping)
print(len(string_stripping))
print(string_stripping.lstrip())
print(len(string_stripping.lstrip()))

# Stripping Whitespace rstrip() function is used to remove the white space in the text ( at the end and at the start) 
string_stripping= "   Programming in Python   "
print(string_stripping)
print(len(string_stripping))
print(string_stripping.strip())
print(len(string_stripping.strip()))

# Avoiding Syntax Errors with Strings
# if we want to use apostrophe then we can use apostrophe inside double quotes
message = "One of Python's strengths is its diverse community."
print(message)

# if we want to use double quotes in the string then we can use double quotes inside single qoutes

message1 = '"One of Python strengths is its diverse community."'
print(message1)


