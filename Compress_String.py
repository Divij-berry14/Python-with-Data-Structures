##INPUT- aaabbccdsa
##OUTPUT- a3b2c2dsa
#
#
#def compress(str1):
#    answer=""
#    str1=str1+"#"
#    count=1
#    for idx in range(1,len(str1)):
#        if(str1[idx]!=str1[idx-1]):
#            answer=answer+str1[idx-1]
#            if(count>1):
#                answer=answer+str(count)
#            count=1
#        else:
#            count+=1
#    return answer
#    
#        
#str1= input()
#print(compress(str1))
#


#yahoo@321
def string_to_integer(n):
    if(n==0):
        return n
    else:
        return string_to_integer(int(n))
n=input()
print(string_to_integer(n))
