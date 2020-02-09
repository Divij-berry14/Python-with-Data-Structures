import sys 

while True:
    n=int(input())
    if n==1:
        n1=int(input())
        n2=int(input())
        print(n1+n2)
    elif n==2:
        n1=int(input())
        n2=int(input())
        print(n1-n2)
    elif n==3:
        n1=int(input())
        n2=int(input())
        print(n1*n2)
        
    elif n==4:
        n1=int(input())
        n2=int(input())
        print(n1//n2)
        
    elif n==5:
        n1=int(input())
        n2=int(input())
        print(n1%n2)
        
    elif n==6:
        sys.exit(0)
    else :
        print("Invalid Operation")

    