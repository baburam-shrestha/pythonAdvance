name=input("Enter your name:")
surname=input("Enter the surname:")
age=int(input("Enter your age:"))
#method 1
print('My name is\t'+name+""+surname+".")
print('My age is ' +str(age)+ 'years old.')

#method 2
#\t is used to print the some space inbetween
#\n is used to print the statement in next line
print(f"My name is\t{name}\t{surname}.\n") 
print(f"My age is\t{age} years old.")

#method 3
full_name1 = "{} {}".format(name, surname)
message1 = f"Hello, {full_name1.title()}!"
print(message1)