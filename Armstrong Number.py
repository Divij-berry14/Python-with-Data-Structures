# def armstrong(number):
#     n = len(str(number))
#     sum = 0
#     # print(n)
#     t = number
#     while(t > 0):
#         temp = t % 10
#         print(temp)
#         sum = sum + pow(temp, n)
#         print(sum)
#         t = int(t/10)
#         print(t)
#     if sum == number:
#         print("True")
#     else:
#         print("False")
#
# number = int(input())
# armstrong(number)

import sys
def NthArmstrong(n):
    count = 0
    for i in range(1, sys.maxsize):
        l = len(str(i))
        sum = 0
        num = i
        while num > 0:
            temp = num % 10
            sum = sum + pow(temp, l)
            num = num//10
        if sum == i:
            count += 1
        if count == n:
            return i

n = int(input())
print(NthArmstrong(n))