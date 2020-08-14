import re
# match=re.match("na","nanp")
# print(match)
# print(match.group())
# string="This is a pet:cat I love cats"
# match=re.search(r"c\w\w\w",string)
# print(match)
# print(match.group())
# string=re.search('\w\w\w\w\we','centre')
# print(string)
# print(string.group())
match=re.search('aa?yushi?','ayushi ayush ') #search for the pattern. In this pattern, the ? checks the previous preceding
# # character and checks if present in the string or not. ? do Matches zero or one occurrence. And in this, the string are
# # ayush and ayushi but the the pattern has aayushi so, ? matches zero or one occurrence, so the starting second a will not the
# #counted and check for the pattern. Output will be ayushi
print(match.group())
# match=re.findall(r'advi[cs]e','I could advise you on your poem, but you would disparage my advice')
# for i in match:
#     print(i)
match=re.search(r'[\w]+@[\w]+\.[\w]+','Please mail it to ayushiwasthere@gmail.com')
print(match.group())