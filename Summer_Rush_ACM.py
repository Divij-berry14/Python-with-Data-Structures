#l, r = [int(l) for l in input().split()]  
#print(l,type(l))
#print(r,type(r))
#i=0
#if(l>=r):
#    print("137")
#while(l<r):
#    if(l%10==9):
#        l=l+1
#    if(l%10==1 or l%10==3 or l%10==7):
#        print(l,end=' ')
#        l=l+1
#    else:
#        l=l+1

#string=input()
#li1=[]
#li=string.split(" ")
#print(li)
#print(type(li))
#print(len(li))
#for i in range(len(li)):
#    temp=li[i]
#    li1.append(temp[::-1])
#    print(temp,li1)
#output=' '.join(li1)
#print(output)

#n = int(input())
#dec = 0
#inc = 0
#same = 2*n - 1
#if(n==1 or n<=0):
#    print("-1")
#for i in range(2*n - 1):
#  a = n
#  for j in range(dec):
#    print(a ,end =' ')
#    a = a - 1
#    
#  for j in range(same):
#    print(a , end =' ')
#    
#  for j in range(inc):
#    a = a + 1
#    print(a , end =' ')
#  
#  if i < n - 1:
#    dec = dec + 1
#    inc = inc + 1
#    same = same - 2
#    
#  else:
#    dec = dec - 1
#    inc = inc - 1
#    same = same + 2
#  
#  print()

#n, x = [int(n) for n in input().split()]  
#li=[int(y) for y in input().split()]
#count=0
#sum=0
##if(0<n<10000):
##    print("-1")
##if(0<x<1000000000):
##    print("-2")
#for i in range(len(li)):
#    sum=sum+li[i]
#    count=count+1
#    if(sum==13 or sum==14):
#        print(count)
#        break
        

    

        