# Files are named locations on disk to store related information
# They are used to permanently store data in a non-volatile memory
# we use files for future use of the data by permanently storing them.
# When we want to read from or write to a file, we need to open it first
# When we are done, it needs to be closed so that the resources that are tied with the file are freed
# file operation takes place in the following order
#   Open a file
    #   open("test.txt", mode='r', encoding='utf-8')
        # Mode	Description
        # r	    Opens a file for reading (default)
        # w	    Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
        # x	    Opens a file for exclusive creation. If the file already exists, the operation fails.
        # a	    Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
        # t	    Opens in text mode. (default)
        # b	    Opens in binary mode.
        # +	    Opens a file for updating (reading and writing)

#   Read or write (perform operation)
        #  we need to open it in write w, append a or exclusive creation x mode.
            # f = open("test.txt",'r',encoding = 'utf-8')
            # f.read(4)
            
            # f.readline()
        #  we must open the file in reading r mode.
            # with open("test.txt",'w',encoding = 'utf-8') as f:
            # f.write("my first file\n")

#   Close the file
    # f.close()

file = open('babu.txt', 'r')
for line in file:
    print (line)


# Python code to illustrate read() mode
file = open("babu.txt", "r")
print (file.read())

# Python code to illustrate read() mode character wise
file = open("babu.txt", "r")
print (file.read(5))

# Python code to create a file
file = open('babu.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

# Python code to illustrate append() mode
file = open('babu.txt','a')
file.write("This will add this line")
file.close()

