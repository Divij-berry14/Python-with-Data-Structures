# 2 4 5 6 7 2   ANS--->2
count=0
li1=[]
n=input()
li=[int(x) for x in input().split()]
length=len(li)
for i in range(0,length,1):
    for j in range(i+1,length,1):
        if(li[i]==li[j]):
            count=count+1
    li1.append(count)
    count=0
print(li1)
for i in range(len(li1)):
    if(li1[i]>=1):
        print(li[i])