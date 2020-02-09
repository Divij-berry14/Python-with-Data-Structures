#FACTORIAL OF A NUMBER
#def fact(a):
#    a_fact=1
#    for i in range(1,a+1,1):
#        a_fact=a_fact*i
#    return a_fact
#
#n=int(input())
#r=int(input())
#n_fact=fact(n)
#r_fact=fact(r)
#n_r_fact=fact(n-r)
#ans=n_fact//(r_fact*n_r_fact)
#print(ans)
 
#def is_prime(n):
#    for d in range(2,n,1):
#        if(n%d==0):
#            break
#    else:
#        return True
#    return False
#
#def primeFrom2toN(n):
#    for k in range(2,n+1,1):
#        #check if k is prime or not, if yes print k
#        is_k_prime=is_prime(k)
#        if(is_k_prime):
#            print(k)
            
#def ncr(n,r):
#    n_fact=fact(n)
#    r_fact=fact(r)
#    n_r_fact=fact(n-r)
#    ans=n_fact//(r_fact*n_r_fact)
#    print(ans)
#ncr(4,2)    

#non-default argument follows default argument
#def f(a=0,b,c):
#    return a+b+c
#f(1,2)

#def checkPalindrome(num):
#    rev=0
#    temp=num
#    while(num!=0):
#        digit=num%10
#        rev=rev*10+digit
#        num=num/10
#    if(rev==temp):
#        return True
#    else:
#        return False
#		
#num = int(input())
#isPalindrome = checkPalindrome(num)
#if(isPalindrome):
#	print('true')
#else:
#	print('false')

# Check if the input number is a part of  Fibonacci series or not

#import math
#def isPerfectSquare(x): 
#    s = int(math.sqrt(x)) 
#    return s*s == x 
#  
#
#def isFibonacci(n): 
#    if isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4):
#        return 1
#    else:
#        return 0
#        
#a=int(input())
#
#
#if isFibonacci(a):
#    print("true")
#else:
#    print("false")

# Palindrome Number FUnction

#def checkPalindrome(num):
#    rev=0
#    temp=num
#    while(num>0):
#        digit=num%10
#        rev=rev*10+(digit*digit*digit)
#        num=num//10
#    if(rev==temp):
#        return 1
#    else:
#        return 0
#		
#num = int(input())
#isPalindrome = checkPalindrome(num)
#if(isPalindrome):
#	print('true')
#else:
#	print('false')


#Armstrong Function

#def checkPalindrome(num):
#    order=len(str(num))
#    temp=num
#    sum=0
#    while(num>0):
#        digit=num%10
#        sum=sum+(digit**order)
#        num=num//10
#    if(sum==temp):
#        return 1
#    else:
#        return 0
#    
#		
#num = int(input())
#isPalindrome = checkPalindrome(num)
#if(isPalindrome):
#	print('true')
#else:
#	print('false')
