
# Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets. 
# The iterator object is initialized using the iter() method. It uses the next() method for iteration.

#     __iter(iterable)__ method that is called for the initialization of an iterator. This returns an iterator object
#     next ( __next__ in Python 3) The next method returns the next value for the Iterable
#     When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an iterator 
#     object which further uses next() method to iterate over. 
#     This method raises a StopIteration to signal the end of the iteration.

company_name = 'Fusemachine Nepal Pvt. Ltd' #string
company_name_character = iter(company_name)
 
while True:
    try:
        character = next(company_name_character)
        print(character)
    except StopIteration:
        break
print("Ends here")

my_list=(10,20,30,40,50,60,70,80,90) #tuple
itr=iter(my_list)
print(next(itr)) #10
print(next(itr)) #20
print(next(itr)) #30
print(next(itr)) #40
print(next(itr)) #50
print(next(itr)) #60
print(next(itr)) #70
print(next(itr)) #80
print(next(itr)) #90
#print(next(itr)) # exception raise StopIteration

my_list=[10,20,30,40,50,60,70,80,90] # list
itrs=iter(my_list)
while True:
    try:
        print(next(itrs))
    except StopIteration:
        break


# An iterable user defined type
class RollNumber:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 10
        return self
 
    def __next__(self):
        x = self.x

        if x > self.limit:
            raise StopIteration
 
        self.x = x + 1
        return x
 
# Prints numbers from 10 to 15
for i in RollNumber(20):
    print(i)
