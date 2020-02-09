# PAIR SUM
#Line 1 : Integer N (Array size)
#Line 2 : Array elements (separated by space)
#Line 3 : Integer x
#Line 1 : Pair 1 elements (separated by space)
#Line 2 : Pair 2 elements (separated by space)
#Line 3 : and so on
#9
#1 3 6 2 5 4 3 2 4
#7
#1 6
#3 4
#3 4
#2 5
#2 5
#3 4
#3 4
n1=input()
li=[int(x) for x in input().split()]
n2=int(input())
length=len(li)
for i in range(length):
    k=i+1
    for j in range(k,length,1):
        if (li[i]+li[j]==n2):
            if(li[i]<li[j]):
                print(li[i],li[j])
            else:
                print(li[j],li[i])
                   
