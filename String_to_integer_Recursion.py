#Input format :
#Numeric string (string, Eg. "1234")
#Output format :
#Corresponding integer (int, Eg. 1234)

#def integer(s):
#    a=len(s)
#    if len(s)==1:
#        return (ord(s[0])-ord('0'))
#    output=integer(s[1:])
#    b=(ord(s[0])-ord('0'))
#    return b*(10**(a-1))+output
#
#    
#s=input()
#k=integer(s)
#print(k)




#def myAtoi(string): 
#    res = 0
#  
#    # Iterate through all characters of input string and  
#    # update result 
#    for i in range(len(string)): 
#        res = res * 10 + (ord(string[i]) - ord('0')) 
#  
#    return res 
#  
## Driver program 
#string = "89789"
#print(string)
#print(myAtoi(string))

#t=int(input())
#for i in range(t):
#    p=0
#    n1=input().split()
#    n,k=int(n1[0]),int(n1[1])
#    li=[int(x) for x in input().split()]
#    l=len(li)
#    li.sort()
#    #print(l)
#    #print(li)
##    if(k<=li[0]):
##        print("No")
#    for j in range(l):
#        temp=k-li[j]
#        if(temp in li):
#            #if(li[j]%)
#            print("Yes")
#            #p+=1
#            #print(p)
#            break
#        elif(l-1==j):
#            print("No")
        


    