s = "geeks quiz practice code"
s1 = s.split(" ")
res = ""
for i in range(len(s1)-1, -1, -1):
    print(i)
    res = res + s1[i] + " "

print(res)
