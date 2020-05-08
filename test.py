a=[[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]
# for i in range(0,len(a)):
#     for j in range(0,len(a[i]),2):
#         x1=a[i][j]
#         y1=a[i][j+1]
#         x2=a[i+1][j]
#         y2=a[i+1][j+1]
#         print(x1,y1,x2,y2,end=" ")
#     print()
for i in range(0,len(a)-1,1):
    li=a[i]+a[i+1]
    # print(str(li))
    x = (li[2] - li[0])
    y = (li[3] - li[1])
    if x!=0:
        div = y / x
    else:
        flag=0
        break
    print(div)
    if i==0:
        slope=div
    if slope==div:
        flag=1
    else:
        flag=0
if flag==0:
    print("false")
else:
    print("true")

# a=[[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]]
# d = {}
# for elem in a:
#     try:
#         d[elem[1]].append(elem[0])
#     except KeyError:
#         d[elem[1]] = [elem[0]]
# print(d)
#
# sum=0
# for w in d.values():
#     sum=sum+w[0]
# print(sum)
# sum1=0
# for w in d.keys():
#     sum1=sum1+w
# print(sum1)