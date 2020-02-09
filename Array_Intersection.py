#Line 1 : Array 1 Size
#Line 2 : Array 1 elements (separated by space)
#Line 3 : Array 2 Size
#Line 4 : Array 2 elements (separated by space)
#Print intersection elements in different lines
#2 6 1 2
#1 2 3 4 2   ANS---> 2 2 1
count=0
li1=[]
n1=input()
li1=[int(x) for x in input().split()]
n2=input()
li2=[int(x) for x in input().split()]
for i in range(len(li1)):
    for j in range(len(li2)):
        if(li1[i]==li2[j]):
            print(li1[i])
            li2[j]=-1
            break
    