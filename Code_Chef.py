s=input()
l=len(s)
if l>1:
    num=0
    temp=l
    for i in range(l-1):
        temp1=ord(s[i])-64
        # print("temp1",temp1)
        num=num+temp1*26**(temp-1)
        # print("num",num)
        temp=temp-1
        # print("temp",temp)
    temp = s[-1]
    res = num + ord(temp)-64
    print(res)
else:
    print(ord(s)-64)


