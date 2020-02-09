n=int(input())
a=0
b=1
if n==0:
    print("0")
if n==1:
    print("1")
elif n==2:
    print("1")
else:
    while(n>1):
        c=a+b
        a=b
        b=c
        n=n-1
print(b)
    
