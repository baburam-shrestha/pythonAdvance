# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
#  For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

def domain_name(url):
    url=url.replace("http://","")
    url=url.replace("https://","")
    url=url.replace("www.","")
    return url.split(".")[0]


print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))