#count() function in an inbuilt function in python programming language 
#that returns the number of occurrences of a substring in the given string.
#string = "geeks for geeks"
#print(string.count("geeks")) 
#2

##Operations on String
#
##SPLIT FUNCTION
#str= "My,name,is,Divij,Berry"
#li=str.split(',',1 )
#print(li)
#
##REPLACE
#str="My,name,is,Divij,Berry, Divij, Divij, Divij"
#str=str.replace("Divij","Jimmy")
#print(str)
#
##FIND
#str= "My,name,is,Divij,Divij,Divij"
#index=str.find("Div",16,20)
#print(index)
#
##LOWER AND UPPER
#str= "My name is Divij Berry"
#str=str.lower()
#print(str)
#str=str.upper()
#print(str)
#
##STARTS WITH
#str= "My name is Divij Berry"
#ans=str.startswith("Die",11,18)
#print(ans)
#

##REPLACE EVERY CHARACTER IN A STRING
#def replace(str,char1,char2):
#    newStr=""
#    for char in str:
#        if char==char1:
#            newStr=newStr+char2
#        else:
#            newStr+=char
#    return newStr
#str="My name is Jimmy Salvatore"
#str=replace(str,"m","o")
#print(str)
#li=[]
#print(li)

#COUNT VOWELS, CONSONANTS, DIGITS, SPECIAL CHARACTER IN A STRING
#def countInString(str):
#    v,c,d,s=0,0,0,0
#    
#    for char in str:
#        if((char>='a' and char<='z') or (char>='A' and char<='Z')):
#            char=char.lower()
#            if(char=='a'or char=='e' or char=='o' or char=='i' or char=='u'):
#                v=v+1
#            else:
#                c=c+1
#        elif(char>='0' and char<='9'):
#            d=d+1
#        else:
#            s=s+1
#    return v,c,d,s

#str="shdbhsbdhsBAHJND3543@#$% kjghjbBHJV12"
#v,c,d,s=countInString(str)
#print(v,c,d,s)


    



#s="divij berry"
#for i in range (len(s)):
#    if(i==0 or i== " "):
#        print(s.capitalize())
#    print(len(s))

#s="divij berry"
#print(' '.join(i.capitalize() for i in s.split(' ')))



