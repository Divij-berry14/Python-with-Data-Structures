# t=int(input())
# for i in range(t):
#     n,c,m=map(int, input().split())
#     num_choc=n//c
#     c = 0
#     temp = 2
#     while(True):
#         if num_choc == m:
#             print(num_choc + 1)
#             break
#         elif num_choc < m:
#             print(num_choc)
#             break
#         if(temp>1):
#             c = c + 1
#             temp = num_choc - m-c
#         else:
#             final_choc = num_choc + m * c
#             print(final_choc)
#             break
s="rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt"
# s1 = s
# d1 = {}
# for i in s1:
#     d1[i] = d1.get(i, 0) + 1
# print(d1)
p = 0
for e in 'hackerrank':
    if e in s[p:]:
        print(e)
        p = s.index(e,p) + 1
    else:
        print('NO')
print("Yes")
