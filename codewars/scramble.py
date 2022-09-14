# Complete the function scramble(str1, str2) 
# that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False


from collections import Counter as cnt
def scramble(s1,s2):
    count = cnt(s1)
   # import ipdb;ipdb.set_trace()
    count.subtract(cnt(s2))
    return (all(e >= 0 for e in count.values()))

    

print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))