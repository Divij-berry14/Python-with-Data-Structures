# t=int(input())
# for _ in range(t):
#     n=int(input())
#     c = 0
#     m = 0
#     for i in range(n):
#         li=[int(x) for x in input().split()]
#         n1=li[0]
#         n11=len(str(n1))
#         n2=li[1]
#         n22=len(str(n2))
#         sum1=0
#         sum2=0
#
#         if n11>1:
#             while(n1>0):
#                 sum1=sum1+int(n1%10)
#                 n1=int(n1//10)
#         else:
#             sum1=n1
#         if n22>1:
#             while(n2>0):
#                 sum2=sum2+int(n2%10)
#                 n2=int(n2//10)
#         else:
#             sum2=n2
#         if sum1>sum2:
#             c=c+1
#         elif sum1<sum2:
#             m=m+1
#         else:
#             c=c+1
#             m=m+1
#     if c>m:
#         print("0",c)
#     elif m>c:
#         print("1",m)
#     else:
#         print("2",c)

# p="outer var"
# def outer():
#     global p
#     print(p)
#     p="inner var"
#     print(p)
# print(p)
# outer()
# print(p)

p="global var"
def outer():
    p="outer var"
    def inner():
        nonlocal p
        print(p)
    print(p)
    inner()
    print(p)

print(p)
outer()
print(p)
