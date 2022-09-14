# data type of variable   can be changed 

integer_variable =5
float_variable=4.55
complex_variable=3+5j
string_variable="Baburam Shrestha"
string_variable1='123141'

#to float
print(type(float(integer_variable)))
# print(type(float(complex_variable))) is not possible
print(type(complex_variable.real)) # it print the real part as float type
print(type(complex_variable.imag)) # it print the imaginary part as float type

#to complex
print(type(complex(integer_variable)))
print(type(complex(float_variable)))

#to integer
print(type(int(float_variable)))
# print(type(int(string_variable))) is not possible but
print(type(int(string_variable1))) # it is possible
# print(type(int(complex_variable))) it is not possible
print(type(int(complex_variable.real)))# it print the real part as integer type
print(type(int(complex_variable.imag))) # it print the imaginary part as integer type

# int, float, and complex to list,tuple,set and dictionary is not possible
print(type(str(integer_variable)))
print(type(str(float_variable)))
print(type(str(complex_variable)))

# int ,float ,complex to string and string to list is possible
print(type(list(str(integer_variable))))
print(type(list(str(float_variable))))
print(type(list(str(complex_variable))))

# int ,float ,complex to string and string to tuple is possible
print(type(tuple(str(integer_variable))))
print(type(tuple(str(float_variable))))
print(type(tuple(str(complex_variable))))

# int ,float ,complex to string and string to dict is  not  possible
# print(type(dict(str(integer_variable))))
# print(type(dict(str(float_variable))))
# print(type(dict(str(complex_variable))))

