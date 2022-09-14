# exceptions can be handled using a try statement.
# The critical operation which can raise an exception is placed inside the try clause. 
# The code that handles the exceptions is written in the except clause.
# We can thus choose what operations to perform once we have caught the exception. 

try:
    #code that may cause exception
    num = int(input("Enter numerator: "))
    den =int (input("Enter denominator: "))
    result = num//den
    print(result)
except:
    print("Divide by zero ")

finally:
    print("finaly blocks")

#Handling multiple exception 
try:
    num = int(input("Enter numerator: "))
    den =int (input("Enter denominator: "))
    result = num//den
    print(result)
    my_list = [1,2,3]
    i = int(input("Enter an index value: "))
    print(my_list[i])

except ZeroDivisionError:
    print("Divide by zero ")
except IndexError:
    print("out of index")
finally:
    print("exceptions block ends here .")