# t=int(input())
# for i in range(t):
#     n = int(input())
#     li = [int(x) for x in input().split()]
#     first = 0
#     last = len(li)-1
#     flag = 0
#     count=li.count(1)
#     print(count)
#     while(first < last and count>0):
#         if li[first] == 1:
#             if li[last] == 1:
#                 distance = last-first
#                 if distance >= 6:
#                     flag = 1
#                 else:
#                     flag = 0
#                     break
#             last=last-1
#         else:
#             first = first+1
#     if flag == 1:
#         print("YES")
#     else:
#         print("NO")
# t=[1,6,12,18]
# # l=[j-i for i, j in zip(t[:-1], t[1:])]  # or use itertools.izip in py2k
# # print(l)
# # li=[]
# for i,j in zip(t[:-1],t[1:]):
#     if j-i>=6:
#         print("Yes")
#         print(j-i)
#     else:
#         print("No")
#         print(j-i)

t=int(input())
for i in range(t):
    n = int(input())
    li = [int(x) for x in input().split()]
    res_list = [i for i, value in enumerate(li) if value == 1]
    if len(res_list)==1:
        print("YES")
        continue
    flag=0
    for i,j in zip(res_list[:-1],res_list[1:]):
        if j-i>=6:
            flag=1
        else:
            flag=0
            break
    if flag==1:
        print("YES")
    else:
        print("NO")
