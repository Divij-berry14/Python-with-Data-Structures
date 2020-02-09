def Rotate(arr, d):
    li1=[]
    for j in range (d,len(arr)):
        li1.append(arr[j])
    for i in range(d):
        li1.append(arr[i])
    print(li1)   

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
d=int(input())
Rotate(arr, d)

