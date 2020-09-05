# def uniqueChars(string):
#     s=list(string)
#     d={}
#     for i in s:
#         d[i]=d.get(i,0)+1
#
#     res=""
#
#     for i in d:
#         res = res+i
#     return res
# # Main
# string = input()
# print(uniqueChars(string))
#
# def uniqueChars(string):
#     m={}
#     res=""
#     for char in string:
#         if char not in m:
#             res=res+char
#             m[char]=True
#     return res
# # Main
# string = input()
# print(uniqueChars(string))



# def longestConsecutiveIncreasingSequence(l):
#     # m = {l[i]: i for i in range(len(l) - 1, -1, -1)}
#     # print(m)
#     d={}
#     for i in l:
#         d[i]=d.get(i,True)
#     print(d)
#     m=0
#     j=0
#     for i in l:
#         start=i
#         end=i
#         j=j+1
#         while(start-1 in d and start==True):
#             start=start-1
#             d[start]=False
#             m=m+1
#         while(end+1 in d and end==True):
#             end=end+1
#             d[end]=False
#             m=m+1
#         if j==1:
#             temp=m
#         if m>temp:
#             max=m
#             temp=m
#     print(d)
#     return max
# n=int(input())
# l=list(int(i) for i in input().strip().split(' '))
# final = longestConsecutiveIncreasingSequence(l)
# print(final)
# # for num in final:
# #     print(num)
#
# #2 12 9 16 10 5 3 20 25 11 1 8 6


# def printPairDiffK(l, k):
#     m={}
#     if k<0:
#         k*=-1
#     for num in l:
#         if num+k in m:
#             for i in range(0,m[num+k]):
#                 print(num,num+k)
#         if k!=0 and num-k in m:
#             print("dict",m[num - k],num)
#             for i in range(0,m[num-k]):
#                 print(num-k,num)
#         if num in m:
#             m[num]+=1
#         else:
#             m[num]=1
#
# n = int(input())
# l = list(int(i) for i in input().strip().split(' '))
# k = int(input())
# printPairDiffK(l, k)



def printPairDiffK(l, k):
    m={}
    for i in l:
        m[i]=m.get(i, 0)+1
    for num in l:
        if num+k in m and m[num+k] > 0:
            temp=m[num]
            while(temp > 0):
                print(num, num+k)
                temp -= 1
                flag1 = True
        if k!=0 and num-k in m and m[num-k]>0:
            temp=m[num]
            while temp>0:
                print(num-k,num)
                temp-=1
                flag2=True
        m[num]=0


n = int(input())
l = list(int(i) for i in input().strip().split(' '))
k = int(input())
printPairDiffK(l, k)





