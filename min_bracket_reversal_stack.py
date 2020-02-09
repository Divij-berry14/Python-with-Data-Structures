#Given a string expression which consists only ‘}’ and ‘{‘. The expression may not be balanced. You need to find the minimum number of bracket reversals which are required to make the expression balanced.
#Return -1 if the given expression can't be balanced.
#
#Sample Input 1 :
#{{{
#
#   Sample Output 1 :
#-1
#
#Sample Input 2 :
#{{{{}}
#
#Sample Output 2 :
#1

def min_bracket_reversal(string):
    if len(string)==0:
        return 0
    if len(string)%2!=0:
        return -1
    s=[]
    for char in string:
        if char=='{' :
            s.append(char)
        else:
            if (len(s)>0 and s[-1]=='{'):
                s.pop()
#            else:
#                s.append(char)
    count=0
    while len(s)!=0:
        c1=s.pop()
        c2=s.pop()
        if c1==c2:
            count=count+1
        else:
            count=count+2
    return count
string=input()
ans=min_bracket_reversal(string)
print(ans)
