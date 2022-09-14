# The rgb function is incomplete
# Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. 
# Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3
def rgb(r, g, b):
    def limit(n):
        if n < 0:
            n = 0
        elif n > 255:
            n = 255
        return n
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))

print(rgb(0,0,0))
print(rgb(1,2,3))
print(rgb(255,255,255))
print(rgb(254,253,252))
print(rgb(-20,275,125))