# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four characters into '#'.

# Examples
# "4556364607935616" --> "############5616"
#      "64607935616" -->      "#######5616"
#                "1" -->                "1"
#                 "" -->                 ""

# // "What was the name of your first pet?"

# "Skippy" --> "##ippy"

# "Nananananananananananananananana Batman!"
# -->
# "####################################man!"

# return masked string
def maskify(cc):
    length=len(cc)
    new_cc=''
    if length<=4:
        return cc
    for i in range(length-4):
        new_cc+="#"
    return new_cc + cc[-4:]
print(maskify('SF$SDfgsd2eA'))
print(maskify('123'))
print(maskify(''))
