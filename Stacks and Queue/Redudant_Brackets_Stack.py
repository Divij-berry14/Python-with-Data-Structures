#Given a string mathematical expression, return true if redundant brackets are present in the expression. Brackets are redundant if there is nothing inside the bracket or more than one pair of brackets are present.
#Assume the given string expression is balanced and contains only one type of bracket i.e. ().
#Note: You will not get partial score for this problem. You will get marks only if all test cases are passed.

#Sample Input 1:
#((a + b)) 

#Sample Output 1:
#true

#Sample Input 2:
#(a+b) 
#Sample Output 2:
#false

def check_redudant_brackets(string):
    s=[]
    flag= False
    for char in string:
        if char !=')' :
            s.append(char)
        else:
            while s[-1]!='(' :
                s.pop()
                flag=True
#                if len(s)==0:
#                    break
#            if len(s)==0:
#                continue
            if flag:
                s.pop()
                flag=False
            else:
                return True
    return False

string=input()
ans=check_redudant_brackets(string)
if ans is True:
    print("True")
else:
    print("False")

