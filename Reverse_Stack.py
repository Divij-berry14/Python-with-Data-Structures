from sys import setrecursionlimit
setrecursionlimit(11000)

def reverse_stack(s1,s2):
    while len(s1)!=1:
        ele=s1.pop()
        s2.append(ele)
    
    last_element=s1.pop()
    
    while len(s2)!=0:
        ele=s2.pop()
        s1.append(ele)
    
    reverse_stack(s1,s2)
    s1.append(last_element)
    
n=int(input())
s1=[int(x) for x in input().split()]
s2=[]
reverse_stack(s1,s2)
while len(s1)!=0:
    print(s1.pop())