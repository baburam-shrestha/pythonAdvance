# Tuples

dimensions = (200, 50)
print(dimensions)
print(type(dimensions))
print(dimensions[0])
print(dimensions[1])

# Looping Through All Values in a Tuple
for dimension in dimensions:
    print(dimension)
    
# Writing over a Tuple
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)