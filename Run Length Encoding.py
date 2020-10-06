def RunLength(s):
    d = {}
    output = ""
    for i in s:
        d[i] = d.get(i, 0) + 1
    for key, value in d.items():
        output = output + key +str(value)
    return output

s = input()
print(RunLength(s))
