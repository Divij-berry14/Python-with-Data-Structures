#1
#12
#123
#1234
n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=i):
        print(j, end='')
        j=j+1
    print()
    i=i+1

#-----------------------------------------------------------------------------
    
#1
#23
#345
#4567
n=int(input())
i=1
k=1
while(i<=n):
    j=1
    k=i
    while(j<=i):
        print(k,end='')
        j=j+1
        k=k+1
    print()
    i=i+1

#------------------------------------------------------------------------------
        
#1
#23
#456
#78910
n=int(input())
i=1
k=1
while(i<=n):
    j=1
    while(j<=i):
        print(k,end='')
        j=j+1
        k=k+1
    print()
    i=i+1

#------------------------------------------------------------------------------

#*****
#****
#***
#**
#*       
    
n=int(input())
i=1
while(i<=n):
    j=n
    while(j>=i):
        print("*",end='')
        j=j-1
    print()
    i=i+1

#------------------------------------------------------------------------------
##       *
##     * *
#    * * *
#  * * * *
#* * * * *
    
n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=n):
        if(j>=n-i+1):
            print("*",end='')
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
    while(spaces<=n-i):
        print(' ',end='')
        spaces=spaces+1
    stars=1
    while(stars<=i):
        print("*",end='')
        stars=stars+1
    print()
    i=i+1