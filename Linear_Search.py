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



