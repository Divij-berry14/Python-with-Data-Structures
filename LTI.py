n=int(input())
li=[int(x) for x in input().split()]
li1=[0,1,2,3,4,5,6,7,8,9]
li2=[0]*n
l=len(li)
for i in range(l):
    if(li[i]%10==li1[0] or li[i]==li1[1] or li[i]==li1[2] or li[i]==li1[3]   or li[i]==li1[4] or li[i]==li1[5] or li[i]==li1[6] or li[i]==li1[7] or li[i]==li1[8] or li[i]==li1[9]):
        print(i)
        print(li[i]%10)
        print(li[i])
        print()
        li2[i]=li[i]

print(li2)
        
        