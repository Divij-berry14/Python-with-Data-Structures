n=int(input())
d=2
flag=False
while d<n :
    if (n%d==0):
        flag=True
    d=d+1
if flag:
    print("Not Prime")
else :
    print("Prime")

##Print Prime number between 2 to N
n=int(input())
k=2
while(k<=n):
    d=2
    flag=False
    while d<k :
        if (k%d==0):
            flag=True
        d=d+1
    if not(flag):
        print(k)
    k=k+1

##Farenhit to Celcius    
S=int(input())
E=int(input())
W=int(input())
while(S<=E):
    C=(S-32)*(5/9)
    print(S,"\t",int(C))
    S=S+W
    #C=0
print("Hello\tWorld")