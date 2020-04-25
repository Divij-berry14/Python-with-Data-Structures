t=int(input())
for i in range(t):
    n,s=map(int,input().split())
    price=[int(x) for x in input().split()]
    players=[int(y) for y in input().split()]
    min_n=min(price)
    index=price.index(min_n)
    price.remove(min_n)
    players.pop(index)
    for j in range(len(price)):
        if players[index]==0:
            if players[j]==1:
                if s+min_n+price[j]<100:
                    flag=1
                    break
                else:
                    flag=0
            else:
                flag=0
        else:
            if players[j]==0:
                if s+min_n+price[j]<100:
                    flag=1
                    break
                else:
                    flag=0
            else:
                flag=0
    if flag==1:
        print("yes")
    else:
        print("no")










