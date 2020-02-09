#List should be sorted for Binary Search

def Binary_Search(li,n1):
    start=0
    end=len(li)-1
    while(start<=end):
        mid=(start+end)//2
        if(li[mid]==n1):
            return mid
            
        elif(li[mid]<n1):
            start=mid+1
        else:
            end=mid-1
    return -1

n=input()
li=[int(x) for x in input().split()]
n1=int(input())
index=Binary_Search(li,n1)
print(index)
