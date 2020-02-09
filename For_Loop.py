#         1
#        232
#       34543
#      4567652 
#
#n=int(input())
#for i in range(1,n+1,1):
#    for s in range(n-i):
#        print(' ',end='')
#    for j in range(i,2*i,1):
#        print(j,end='')
#    for j in range(2*i-2,i-1,-1):
#        print(j,end='')
#    print()

#------------------------------------------------------------------------------

#11111
#0000
#111
#00
#1
#
#n=int(input())
#i=1
#k=n
#while(i<=n):
#    j=1
#    if(i%2==0):
#        while(j<=k):
#            print('0',end='')
#            j=j+1
#    else:
#        while(j<=k):
#            print('1',end='')
#            j=j+1
#    print()
#    i=i+1
#    k=k-1
#                                 OR
#n=int(input())
#k=n
#for i in range(1,n+1,1):
#    if(i%2==0):
#        for j in range(1,k+1,1):
#            print('0',end='')
#    else:
#        for j in range(1,k+1,1):
#            print('1',end='')
#    print()
#    k=k-1

#-------------------------------------------------------------------------------
#
#   *
#  ***
# *****
#*******
# *****
#  ***
#   *
#n=int(input())
#n1=(n+1)/2
#n2=n/2
#i=1
#k=0
#while(i<=n1):
#    spaces=1
#    while(spaces<=n1-i):
#        print(' ',end='')
#        spaces=spaces+1
#    j=1
#    while(j<=i+k):
#        print('*',end='')
#        j=j+1
#    print()
#    i=i+1
#    k=k+1
#i=1
#k=n-2
#while(i<=n2):
#    spaces=1
#    while(spaces<=i):
#        print(' ',end='')
#        spaces=spaces+1
#    j=1
#    while(j<=k):
#        print('*',end='')
#        j=j+1
#    print()
#    i=i+1
#    k=k-2

#-----------------------------------------------------------------------------
#
#123456
# 23456
#  3456
#   456
#    56
#     6
#n=int(input())
#i=1
#k=n
#while(i<=n):
#    spaces=1
#    p=i
#    while(spaces<i):
#        print(' ',end='')
#        spaces=spaces+1
#    j=1
#    while(j<=k):
#      print(p," ",end='')
#      j=j+1
#      p=p+1
#    print()
#    i=i+1
#    k=k-1
#i=1
#while(i<=n-1):
#    spaces=2
#    p=n-i
#    while(spaces<=n-i):
#        print(' ',end='')
#        spaces=spaces+1
#    j=1
#    while(j<=i+1):
#        print(p," ",end='')
#        j=j+1
#        p=p+1
#    print()
#    i=i+1
#    k=k-2

#------------------------------------------------------------------------------

#1    2   3    4   5
# 11   12  13   14  15
# 21   22  23   24  25
# 16   17  18   19  20
# 6    7    8   9   10
n=int(input())
for i in range(1,n+1,2):
    temp=n*i
    for j in range(temp-n+1,temp+1):
        print(j,end=" ")
    print()
    
n1=0
if n%2!=0:
    n1=n-1
else:
    n1=n
for k in range(n1,1,-2):
    temp=k*n
    for m in range(temp-n+1,temp+1):
        print(m,end=" ")
    print()

#------------------------------------------------------------------------------

#4444444
#4333334
#4322234
#4321234
#4322234
#4333334  
#4444444

n = int(input())
dec = 0
inc = 0
same = 2*n - 1
for i in range(2*n - 1):
  a = n
  for j in range(dec):
    print(a, end = '')
    a = a - 1
    
  for j in range(same):
    print(a, end = '')
    
  for j in range(inc):
    a = a + 1
    print(a, end = '')
  
  if i < n - 1:
    dec = dec + 1
    inc = inc + 1
    same = same - 2
    
  else:
    dec = dec - 1
    inc = inc - 1
    same = same + 2
  
  print()