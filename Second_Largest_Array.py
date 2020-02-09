n=int(input())
count=0
li=[int(x) for x in input().split()]
length=len(li)
li.sort(reverse = True)
min=li[0]
for j in range(length-1):
    if(li[j]==li[j+1]):
        count=count+1
if(count+1==len(li)):
    print("-2147483648")
for i in range(1,n):
    if(min>li[i]):
        print(li[i])
        break
