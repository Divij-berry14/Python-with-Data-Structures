prime = 101
def patternMatching(text, pattern):
    m = len(pattern)
    n = len(text)
    patternHash = createHash(pattern, m)
    textHash = createHash(text, m)

    for i in range(n-m+1):
        if patternHash == textHash:
            if checkEqual(text[i:i+m], pattern[0:]) is True:
                return i
        if i<n-m:
            textHash = reHash(text, i, i+m, textHash, m)
    return -1

def checkEqual(str1,str2):
    if len(str1)!=len(str2):
        return False
    i = 0
    j = 0
    for i, j in zip(str1, str2):
        if i != j:
            return False
    return True

def createHash(input,end):
    hash = 0
    for i in range(end):
        hash = hash + ord(input[i]) * pow(prime, i)
    return hash

def reHash(input, oldIndex, newIndex, oldHash, patternLen):
    newHash = oldHash - ord(input[oldIndex])
    newHash = newHash/prime
    newHash += ord(input[newIndex])*pow(prime, patternLen - 1)
    return newHash

index = patternMatching("TusharRoy", "sharRoy")
print("Index ", index)
index = patternMatching("TusharRoy", "Roy")
print("Index ", index)
index = patternMatching("TusharRoy", "shar")
print("Index ", index)
index = patternMatching("TusharRoy", "usha")
print("Index ", index)
index = patternMatching("TusharRoy", "Tus")
print("Index ", index)
index = patternMatching("TusharRoy", "Roa")
print("Index ", index)