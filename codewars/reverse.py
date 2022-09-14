
# function to return the reversed each word in string and include spaces.
# Step 1: Input a string and store it in a variable s

# Step 2: Then split the string into a list of words using the built-in function 'split()'

# Step 3: Reverse each word and store them in a new list nw

# Step 4: Join the new list of words and make a new string ns
def reverse_words(text):
    word_lists=text.split(" ")
    reserved_word_lists= [word_list[::-1] for word_list in word_lists ]

    reverse_word=' '.join([str(reserved_word_list) for reserved_word_list in reserved_word_lists])

    return reverse_word
print(reverse_words('double  spaced  words'))
