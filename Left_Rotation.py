#Sample Input
#5 4
#1 2 3 4 5
#
#Sample Output
#5 1 2 3 4

inp=input().split()
n,d=int(inp[0]),int(inp[1])
li=list(map(int,input().split()))
#print(li)
li1=[0]*(n)
print(li1)
for i in range(len(li)):
    index=i-4
    li1[index]=li[i]
    print(li)
    print(li1)
    print(index-i)
print(*li1)
    