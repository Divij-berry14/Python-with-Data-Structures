# t=int(input())
# for i in range(t):
#     string1=list(input())
#     k=int(input())
#     x=int(input())
#     d={}
#     for w in string1:
#         d[w]=d.get(w,0)+1
#     j=0
#     for w in d:
#         if d[w]>x and j<=k:
#             d[w]=d[w]-1
#             j=j+1
#     print(d)
#     c=0
#     for w in d:
#         if d[w]<=x:
#             c=c+1
#     print(c)

# n=int(input())
# zero=["1"]
# for i in range(n-1):
#     zero.append("0")
# number="".join(zero)
# num=int(number)
# while(num>0):
#     if num%3==0 and num%7==0:
#         print(num)
#         break
#     else:
#         num=num+1

inp=input().split()
n,q=int(inp[0]),int(inp[1])
li=[int(x) for x in input().split()]
index=li.index(li[0])
li.insert(index,0)
for i in range(q):
    q0=input().split()
    if q0[0]==1:
        q00,q01,q02=int(q0[0]),int(q0[1]),int(q0[2])
        li[q01 + 1] = li[q01] + q02
    else:
        q1 = int(q0[1])
        sum = 0
        for j in range(1, len(li)):
            sum = sum + (li[j] * (q1 % j))
        print(sum)









