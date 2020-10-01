# import dis
# print(dis.dis('for _ in [1,2,3]:pass'))

# li = [5, 7,  22, 97, 54, 62, 77, 23, 73, 61]
# res = filter(lambda x: (x%2 != 0), li)
# for i in res:
#     print(i)
# print(list(res))
# print(list(map(lambda x:x%2==0,range(0,10))))
# print(list(filter(lambda x:x*2,range(0,10))))
# def func(li):
#     li.append(8)
#
# li=[1,5]
# func(li)
# print(li)
# s1 = "dog is"
# s2 = "aa"# print(len(s1))
# print(len(s2))
# def fun(li):
#     li.append("11")
#     li.append("100")
# li = [1,2,3,4,5]
# fun(li)
# print(li)

s = " geeks quiz practice code"
s1 = s.split(" ")
print(s1)
res = ""
for i in range(len(s1)-1, -1, -1):
    res = res + " " + s1[i]
print(res)

# Python3 program to reverse a string
# s = input()
# s = "i like this program very much"
# words = s.split(' ')
# string =[]
# for word in words:
# 	string.insert(0, word)
# print(string)
# print("Reversed String:")
# print(" ".join(string))


# Recursive python program to reverse an array

# Function to reverse A[] from start to end
# def reverseList(A, start, end):
# 	if start >= end:
# 		return
# 	A[start], A[end] = A[end], A[start]
# 	return reverseList(A, start+1, end-1)
#
# # Driver function to test above function
# A = [1, 2, 3, 4, 5, 6]
# print(A)
# A = reverseList(A, 0, 5)
# print("Reversed list is")
# print(A)

