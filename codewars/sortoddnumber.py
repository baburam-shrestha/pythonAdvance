# You will be given an array of numbers
# You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
def sort_array(source_array):
    # Return a sorted array
    length=len(source_array)
    for i in range(length):
        if source_array[i] % 2 == 1:
            for j in range(i+1,length):
                if source_array[j] % 2 == 1:
                    if source_array[i] > source_array[j]:
                        min=source_array[j]
                        source_array[j]=source_array[i]
                        source_array[i]=min
    return source_array
print([5, 3, 2, 8, 1, 4])
print(sort_array([5, 3, 2, 8, 1, 4]))
print([5, 3, 1, 8, 0])
print(sort_array([5, 3, 1, 8, 0]))
print(sort_array([]))
