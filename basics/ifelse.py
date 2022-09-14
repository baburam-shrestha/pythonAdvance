# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")

# If the number is negative, we print an appropriate message
num = -1
if num > 0:
    print(num, "is a negative number.")


# If the number is positive/negative, we print an appropriate message
number=5
if number>0:
    print(num, "is a positive number.")
else:
    print(num, "is a negative number.")


# If the number is positive/negative/zero, we print an appropriate message
number=int(input("Enter number:"))
if number>0:
    print(number, "is a positive number.")
elif number<0:
    print(number,"is a negative number.")
else:
    print(number, "is a zero number.")