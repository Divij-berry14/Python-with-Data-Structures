t = int(input())
for i in range(t):
    n=int(input())
    sum=0
    li1=[int(x) for x in input().split()]
    li2=[int(y) for y in input().split()]
    for i in range(len(li1)):
        if li1[i]==li2[i]:
            sum=sum+li1[i]
    print(sum)

