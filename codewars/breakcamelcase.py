# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""


def solution(s):
    return "".join([" " + string1 if string1.isupper() else string1 for string1 in s])