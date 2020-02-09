#
#
## Complete the migratoryBirds function below.
#def migratoryBirds(arr):
#    d={}
#    for c in arr:
#        if( c in d):
#            d[c]=d[c]+1
#        else:
#            d[c]=1
#    for c1 in d:
#        if(d[c1]==1):
#            print(c1)
#            
#
#    
#
#
#arr_count = int(input().strip())
#
#arr = list(map(int, input().rstrip().split()))
#
#migratoryBirds(arr)

#s1=input()
#s2=input()
#s3=[]
#for i in range(len(s1)):
#    s3.append(s1[i])
#    #print(s3)
#
##s3.pop()
#s2=list(s2)
##print(list(s2))   
#print(s1)
#print(s2)
#print(s3)
#!/bin/python3


# Complete the icecreamParlor function below.
#def icecreamParlor(m, arr):
#    arr.sort()
#    l=len(arr)
#    j=l-1
#    for i in range(l):
#        if(arr[i]+arr[j]==m):
#            print(i+1,j+1,end="")
#        else:
#            j=j-1
#
#
#
#
#t = int(input())
#
#for t_itr in range(t):
#    m = int(input())
#
#    n = int(input())
#
#    arr = list(map(int, input().rstrip().split()))

#    result = icecreamParlor(m, arr)

#test_str = "Geeks"
#res = [test_str[i: j] for i in range(len(test_str))for j in range(i + 1, len(test_str) + 1)]
#print(set(test_str))
#s=input()
#n=int(input())
#l=len(s)
#value=n//l
#temp=s[:n%l]
#s=s*value
#s=s+temp
##print(temp)
#print(s)
#c=s.count("a")
#print(c)
#print(new_s)


#list(new_s)
#print(new_s)
#l1=len(new_s)
#if(len(new_s)<n):
#    temp=n-l1
#    new_s.append(s[:temp])
#new_s1="".join(map(str, new_s))
#print(new_s1)
#c=new_s.count('a')
#print(value)
#print(new_s)
#print(c)

#!/bin/python3

#import math
#import os
#import random
#import re
#import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    l=len(c)
    count=0
    #temp=0
    i=0
    while(i<=l-2):
        print(i)
        if(c[i]==0 and c[i+2]==0):
            if(c[i+1]==0):
                #temp=temp+2
                i=i+2
                print("i1",i)
            count=count+1
            print(count)
        if(c[i]==0 and c[i+2]==1):
            count=count+1
            i=i+1
            print("i2",i)
        print("i3",i)
    print("i4",i)
    print(count)
            
    return count



if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print("value",result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
