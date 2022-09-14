# Literal is a raw data given in a variable or constant. 
# In Python, there are various types of literals they are as follows:
# Numeric literals,String literals, Boolean Literals,Special literals

#Numeric Literals are immutable (unchangeable).
#Numeric literals can belong to 3 different numerical types: Integer, Float, and Complex.

#Integer literal
a = 0b1010  #Binary Literal
b = 100     #Decimal Literal
c = 0o310   #Octal Literal
d = 0x12c   #Hexadecimal Literal
print(f"{a}\n{b}\n{c}\n{d}")

#Float literal
float_1 = 10.5 
float_2 = 1.5e2
print(float_1, float_2)

#Complex literal 
x = 1+3.1415j
print(x,x.real,x.imag)