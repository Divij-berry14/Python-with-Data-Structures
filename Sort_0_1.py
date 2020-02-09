#n=input()
#li=[int(x) for x in input().split()]
#length=len(li)
#for i in range(length):
#    k=i+1
#    for j in range(k,length):
#        if(li[i]<li[j]):
#            print(li[i],end=' ')

n=input()
li=[int(x) for x in input().split()]
li.sort()
for i in li:
    print(i,end=' ')
            
#n=int(input())
#li=[int(x) for x in input().split()]
#li.sort(reverse = True)
#min=li[0]
#for i in range(1,n):
#    if(min>li[i]):
#        print(li[i])
#        break