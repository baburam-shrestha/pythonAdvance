# A namespace is a collection of names.

# In Python, you can imagine a namespace as a mapping of every name you have defined to corresponding objects.

# Different namespaces can co-exist at a given time but are completely isolated.

# A namespace containing all the built-in names is created when we start the Python interpreter and 
# exists as long as the interpreter runs.

# This is the reason that built-in functions like id(), print() etc. 
# are always available to us from any part of the program. Each module creates its own global namespace.

# These different namespaces are isolated.
# Hence, the same name that may exist in different modules does not collide.

# Modules can have various functions and classes. 
# A local namespace is created when a function is called, which has all the names defined in it
# Similar is the case with class. The following diagram may help to clarify this concept.