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
# t=int(input())
# for _ in range(t):
#     s=input()
#     x=0
#     i=0
#     while(i<len(s)-1):
#         if (s[i]=='x' and s[i+1]=='y') or (s[i]=='y' and s[i+1]=='x'):
#             x += 1
#             i += 2
#         else:
#             i += 1
#     print(x)
t = int(input())
for _ in range(t):
    n=int(input())
    li=[int(x) for x in input().split()]
    flag=0
    if li[0] == 5:
        # sum = 5
        # fiveCount=li.count(5)
        # print(fiveCount)
        fiveCount=1
        for i in range(1, len(li)):
            if li[i] != 5:
                s = li[i]-5
                moneyBack = s//5
                if moneyBack <= fiveCount:
                    fiveCount = fiveCount - moneyBack
                    flag = 1
                else:
                    flag = 0
                    # print("NO")
                    # break
            else:
                fiveCount += 1
        if flag == 1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
