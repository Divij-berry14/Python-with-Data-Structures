n=int(input())
if (n%2==0):
    print("n is even")

else:
    print("n is odd")
a=True
if a:
    print("i am inside if")
else:
    print("inside else")
n=int(input())
if n>10:
    print("red")
elif n>=5 and n<=10:
    print("green")
elif n>0 and n<5:
    print("yellow")
n=int(input())
if n>10:
    print("Positive")
elif n==0:
    print("Zero")
else:
    print("Negative")
if (10 < 0) and (0 < -10):
    print("A")
elif (10 > 0) or False:
    print("B")
else:
    print("C")
if True or True:
    if False and True or False:
        print('A')
    elif False and False or True and True:
        print('B')
    else:
      print('C')
else:
     print('D')
n=int(input())
sum=0
count=1
while(count<=n):
    if(count%2==0):
        sum=sum+count
    count=count+1
    
print(sum)
    
