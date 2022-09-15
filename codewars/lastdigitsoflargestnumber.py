# Define a function that takes in two non-negative integers aaa and bbb and returns the last decimal digit of aba^ba 
# Note that aaa and bbb may be very large!

# For example, 

# Examples
# last_digit(4, 1)                # returns 4
# last_digit(4, 2)                # returns 6
# last_digit(9, 7)                # returns 9
# last_digit(10, 10 ** 10)        # returns 0
# last_digit(2 ** 200, 2 ** 300)  # returns 6

def last_digit(n1, n2):
    if n1 == 0 and n2 == 0:
        return 1
    if n2 == 0:
        return 1
    if n1 == 0:
        return 0
    # if exponent is divisible by 4 that means last digit will be pow(n1), 4) % 10.
    # if exponent is not divisible by 4 that means last digit will be pow(n1, n2%4) % 10
    if n2 % 4 == 0:
        res = 4
    else:
        res = n2 % 4  
    # Find last digit in 'n1' and compute its exponent
    num = pow(n1, res)
    return num % 10

print(last_digit(4, 1))
print(last_digit(4, 2))
print(last_digit(9, 7))
print(last_digit(10, 10 ** 10))
print(last_digit(2 ** 200, 2 ** 300))
print(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651))
