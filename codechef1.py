def uniqueChars(string):
    s=list(string)
    d={}
    for i in s:
        d[i]=d.get(i,0)+1

    res=""

    for i in d:
        res = res+i
    return res
# Main
string = input()
print(uniqueChars(string))

def uniqueChars(string):
    m={}
    res=""
    for char in string:
        if char not in m:
            res=res+char
            m[char]=True
    return res
# Main
string = input()
print(uniqueChars(string))
