t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    li=[int(x) for x in input().split()]
    s=sum(li)
    sum1=0
    for i in range(len(li)):
        if li[i] > k:
            sum1=sum1 + k
        else:
            sum1=sum1+li[i]
    # print(sum1)
    res=s-sum1
    print(res)
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
        tenCount=0
        fi5teenCount=0
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
t = int(input())
for _ in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    curr,flag = li[0],0
    if(curr != 5):
        print("NO")
        continue
    money = [1,0]
    for i in range(1,len(li)):
        if(li[i] == 5):
            money[0]+=1
        elif(li[i] == 10):
            if(money[0] != 0):
                money[0]-=1
            else:
                flag = 1
                break
        elif(li[i] == 15):
            if(money[1] != 0):
                money[1]-=1
            elif(money[0] >= 2):
                money[0]-=2
            else:
                flag = 1
                break
    if(flag == 1):
        print("NO")
    else:
        print("YES")

t = int(input())
for _ in range(t):
    n = int(input())
    if n%2==0:
        n=n//2
        n=n-1
        print(n//2)
    else:
        n=n-1
        print(n//2)

