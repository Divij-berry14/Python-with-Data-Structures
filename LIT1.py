n=int(input())
li=[int(x) for x in input().split()]
li1=[0,1,2,3,4,5,6,7,8,9]
li2=[0]*n
l=len(li)
li3=[]
li4=[]
i=0
for i in range(l):
    a=li[i]%10
    if(a%10==li1[0] or a==li1[1] or a==li1[2] or a==li1[3]   or a==li1[4] or a==li1[5] or a==li1[6] or a==li1[7] or a==li1[8] or a==li1[9]):
        li3.append(a)
        
li3.sort(reverse=True)
print(li3)
            

        
        
             
             

        