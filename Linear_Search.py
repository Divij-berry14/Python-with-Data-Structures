n=input()
li=[int(x) for x in input().split()]
find=int(input())
for i in range(len(li)):
    if li[i]==find:
        print(i)
        break
else:
    print("-1")

#                              OR
isFound=False
n=input()
li=[int(x) for x in input().split()]
find=int(input())
for i in range(len(li)):
    if li[i]==find:
        print(i)
        isFound=True
        break

if isFound is False:
    print('-1')
    
#LINEAR SEARCH THROUGH FUNCTION
def Linear_Search(li,find):
    for i in range(len(li)):
        if li[i]==find:
            return i
    return -1

li=[int(x) for x in input().split()]
find=int(input())
index=Linear_Search(li,find)
print(index)

# REVERSE A LIST
def reverse_l(li):
    length=len(li)
    for i in range(length//2):
        li[i],li[length-i-1]=li[length-i-1],li[i]
li=[1,2,3,4,5,6]
reverse_l(li)
print(li)

#                        OR
def reverse_l(li):
    length=len(li)
    for i in range(length//2):
        li[i],li[-i-1]=li[-i-1],li[i]
li=[1,2,3,4,5,6]
reverse_l(li)
print(li)


li1=[12,34,56,7,8,9,78]
print(li1[::-1])   
print(li1[3::-1]) 
print(li1[:1:-1])       
        

 Swap Alternative
n=input()
li=[int(x) for x in input().split()]
length=len(li)
for i in range(0,length,2):
    if i<length-1:
        li[i],li[i+1]=li[i+1],li[i]
print(*li)  # print(*li) is used to print the elements of the iterable in a single line
for i in li:
    print(i,end=' ')


