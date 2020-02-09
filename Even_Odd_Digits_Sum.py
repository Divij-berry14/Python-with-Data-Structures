## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
n=int(input())
sum=0
sum1=0
while(n>0):
    digit=n%10
    if(digit%2==0):
        sum=sum+digit
    else:
        sum1=sum1+digit
    n=n//10
print(sum,"",sum1)    