def cap(word):
    return word[1:].islower() or word.islower() or word.isupper()





s=input()
res=cap(s)
print(res)