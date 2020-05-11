trust=[[1,3],[1,4],[2,3],[2,4],[4,3]]
# [[1,3],[2,3],[3,1]]
for i in range(len(trust)):
    if i==0:
        a=trust[i][0]
        b=trust[i][1]
        c=b
        continue
    a1=trust[i][0]
    b1=trust[i][1]
    if a==a1:
        if b==b1:
            mark1=b1
    else:
        if b==b1:
            mark1=b1
        elif b==a1:
            flag=0

# # for i in range(0,len(a)):
# #     for j in range(0,len(a[i]),2):
# #         x1=a[i][j]
# #         y1=a[i][j+1]
# #         x2=a[i+1][j]
# #         y2=a[i+1][j+1]
# #         print(x1,y1,x2,y2,end=" ")
# #     print()
# for i in range(0,len(a)-1,1):
#     li=a[i]+a[i+1]
#     # print(str(li))
#     x = (li[2] - li[0])
#     y = (li[3] - li[1])
#     if x!=0:
#         div = y / x
#     else:
#         flag=0
#         break
#     print(div)
#     if i==0:
#         slope=div
#     if slope==div:
#         flag=1
#     else:
#         flag=0
# if flag==0:
#     print("false")
# else:
#     print("true")
#
