# Your task is to make a function that can take any non-negative integer as an 
# argument and return it with its digits in descending order. 
# Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

def descending_order(num):
    # Bust a move right here
    num_str= str(num)
    num_list=[]
    for num_char in num_str:
        num_list.append(int(num_char))
    number_list=sorted(num_list, reverse=True)

    string_number=''
    for number in number_list:
        string_number+=str(number)
    return int(string_number)

print(descending_order(23))
print(descending_order(51))
print(descending_order(123456789))
print(descending_order(12343452789))


