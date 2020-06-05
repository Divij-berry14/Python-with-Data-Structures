# t=int(input())
# for _ in range(t):
#     n,k=map(int,input().split())
#     li=[int(x) for x in input().split()]
#     s=sum(li)
#     sum1=0
#     for i in range(len(li)):
#         if li[i] > k:
#             sum1=sum1 + k
#         else:
#             sum1=sum1+li[i]
#     # print(sum1)
#     res=s-sum1
#     print(res)
t=int(input())
for _ in range(t):
    s=input()
    x=0
    i=0
    while(i<len(s)-1):
        if (s[i]=='x' and s[i+1]=='y') or (s[i]=='y' and s[i+1]=='x'):
            x += 1
            i += 2
        else:
            i += 1
    print(x)