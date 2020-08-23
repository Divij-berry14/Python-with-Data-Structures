string1 = input()
string2 = input()
k = int(input())
res=""
new_li=[]
for i in range(len(string1)):
    if ord(string1[i])+k>=ord("z"):
        temp1 = ord("z")-ord(string1[i])
        temp2 = ord(string2[i])
        if abs(temp1 - temp2) <= k:
            flag = True
        else:
            flag = False
    else:
        temp1 = ord(string1[i])
        temp2 = ord(string2[i])
        if abs(temp1 -temp2) <= k:
            flag = True
        else:
            flag = False

if flag:
    print("Yes")
else:
    print("No")



