
# Generator-Function
# A generator-function is defined like a normal function, but whenever it needs to generate a value, 
# it does so with the yield keyword rather than return. If the body of a def contains yield, 
# the function automatically becomes a generator function.
#a generator function returns an generator object that is iterable, i.e., can be used as an Iterators .


print("Generator-Function")
def functionGeneratorFun():
    yield 1            
    yield 2            
    yield 3            

for value in functionGeneratorFun(): 
    print(value)

# Generator-Object
# Generator functions return a generator object
# Generator objects are used either by calling the next method on the generator object or
# using the generator object in a “for in” loop

print("Generator-Object")
def objectGeneratorFun():
    yield 1
    yield 2
    yield 3
   
x = objectGeneratorFun()
print(next(x))
print(next(x))
print(x.__next__())


#generator expression
a = (x*x for x in range(10))
print(next(a))
print(next(a))
print(next(a))
print(a.__next__())

exp = (x*x for x in range(2,9,1))
while True:
    try:
        square = exp.__next__()
        print(square)
    except StopIteration:
        break
print("Ends here")

