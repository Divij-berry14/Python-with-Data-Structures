# str = "This is a test string".lower()
# word = "tsit"
# ans = len(str)
# for i in word:
#     ans = min(ans, str.count(i)//word.count(i))
# print(ans)

import sys
test_str = "This is a test string"
test_str = test_str.lower()
word = "tsit"

res = {}
word_count = {}


for keys in word:
  if keys != ' ':
    word_count[keys] = word_count.get(keys, 0) + 1


for keys in test_str:
  if keys != ' ':
    res[keys] = res.get(keys, 0) + 1

ans = sys.maxsize

print(word_count)
print(res)

for keys in word_count:
    if keys in res:
        a = res[keys]    #checking if the key exists in the res or not
    else:
        ans = 0   # if the char does not exist in the string then ans = 0
        break
    b = word_count[keys]
    n = a//b
    if n < ans:   # finding the lowest of the requirement
        ans = n
print(ans)

