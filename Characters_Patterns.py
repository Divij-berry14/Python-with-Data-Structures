#Print kth Character
k=int(input())
x=ord("A")
asciiTarget=x+k-1
targetChar=chr(asciiTarget)
print(targetChar)

#------------------------------------------------------------------------

ABCD
ABCD
ABCD
ABCD
ABCD
#
n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=n):
        charP= chr(ord('A') + j-1)
        print(charP,end='')
        j=j+1
    print()    
    i=i+1

##------------------------------------------------------------------------------
    
ABCD
BCDE
CDEF
DEFG

n=int(input())
i=1
while(i<=n):
    j=1
    start_char=chr(ord("A") + i-1)
    while(j<=n):
        charP= chr(ord(start_char) + j-1)
        print(charP,end='')
        j=j+1
    print()    
    i=i+1
#
##------------------------------------------------------------------------------
#    
##12345
##1234
##123
##12
##1
#    
n=int(input())
i=1
while(i<=n):
    k=1
    j=n
    while(j>=i):
        print(k,end='')
        j=j-1
        k=k+1
    print()
    i=i+1
    
##-------------------------------------------------------------------------------
#
##A
##BB
##CCC
##DDDD
    
n=int(input())
i=1
while(i<=n):
    j=1
    start_char=chr(ord("A") + i-1)
    while(j<=i):
        #charP= chr(ord(start_char) + j-1)
        print(start_char,end='')
        j=j+1
    print()    
    i=i+1

##----------------------------------------------------------------------------
#
##1
##11
##202
##3003    
##40004

n=int(input())
i=1
while(i<=2):
    j=1
    while(j<=i):
        print("1",end='')
        j=j+1
    print()
    i=i+1
i=3
while(i<=n):
    j=1
    while(j<=i):
        if (i==j or j==1):
            print(i-1,end='')
        else:
            print("0",end='')
        j=j+1
    print()
    i=i+1

##----------------------------------------------------------------------------
#
##1
##11
##121
##1221
##12221    

n=int(input())
i=1
while(i<=2):
    j=1
    while(j<=i):
        print("1",end='')
        j=j+1
    print()
    i=i+1
i=3
while(i<=n):
    j=1
    while(j<=i):
        if (i==j or j==1):
            print(1,end='')
        else:
            print("2",end='')
        j=j+1
    print()
    i=i+1

##------------------------------------------------------------------------------
#    
##      1
##     12
##    123
##   1234
##  12345 

n=int(input())
i=1
while(i<=n):
    j=1
    k=1
    while(j<=n):
        if(j>=n-i+1):
            print(k,end='')
            k=k+1
        else:
            print(" ",end='')
        j=j+1
    print()
    i=i+1
 
                                         #OR

n=int(input())
i=1
while(i<=n):
    spaces=1
    #spaces
    while(spaces<=n-i):
        print(' ',end='')
        spaces=spaces+1
    p=1
    j=1
    #increasing sequences
    while(j<=i):
        print(p,end='')
        p=p+1
        j=j+1
    print()
    i=i+1
##------------------------------------------------------------------------------    
##      1
##     121
##    12321
##   1234321
##  123454321 

n=int(input())
i=1
while(i<=n):
    spaces=1
    #spaces
    while(spaces<=n-i):
        print(' ',end='')
        spaces=spaces+1
    p=1
    j=1
    #increasing sequences
    while(j<=i):
        print(p,end='')
        p=p+1
        j=j+1
    #decreasing sequence
    p=i-1
    while(p>=1):
        print(p,end='')
        p=p-1
    print()
    i=i+1

##------------------------------------------------------------------------------
#    
##1      1
##12    21
##123  321
##12344321
    
n=int(input())
totalspace=n*2-2
row=1
while(row<=n):
    column=1
    while(column<=row):
        print(column,end='')
        column=column+1
    space=1
    while(space<=totalspace):
        print(" ",end='')
        space=space+1
    totalspace=totalspace-2
    column=row
    while(column>0):
        print(column,end='')
        column=column-1
    row=row+1
    print()
    

#      1
#     212
#    32123
#   4321234
#  543212345

n=int(input())
i=1
while(i<=n):
    spaces=1
    while(spaces<=n-i):
        print(" ",end='')
        spaces=spaces+1 
    j=i
  #left triangle 
    while(j>0):
        print(j,end='')
        j=j-1
#right triangle
    p=2
    while(p<i+1):
        print(p,end='')
        p=p+1
    i=i+1
    print()    

#-----------------------------------------------------------------------------
    
#*
# * *
#   * * *
#     * * * *
#   * * *
# * *
#*

n=int(input())
i=1
n1=(n+1)/2
n2=n/2
while(i<=n1):
    spaces=1
    while(spaces<i):
        print(' ',end='')
        spaces=spaces+1
    j=1
    #upper triangle
    while(j<=i):
        print("* ",end='')
        j=j+1
    print()
    i=i+1
i=1
while(i<=n2):
    spaces=1
    while(spaces<=n2-i):
        print(" ",end='')
        spaces=spaces+1
    j=1
    while(j<=n2-i+1):
        print("* ",end='')
        j=j+1
    print()
    i=i+1

#------------------------------------------------------------------------------

#*000*000*
#0*00*00*0
#00*0*0*00
#000***000

n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=2*n+1):
        if(j==i or j==2*(n+1)-i or j==n+1):
            print("*",end='')
            j=j+1
        else:
            print("0",end='')
            j=j+1
    print()
    i=i+1
    
