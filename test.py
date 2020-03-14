import math
t=int(input())
for _ in range(t):
    n=int(input())
    i=1
    sum=0
    num=n
    while(i<=num):
        if i!=n:
            if num%i==0:
                sum=sum+i
        i=i+1
    if sum==n:
        print("Yes")
    else:
        print("No")
