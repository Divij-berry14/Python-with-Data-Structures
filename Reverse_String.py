s = "geeks quiz practice code"
s1 = s.split(" ")
res = ""
print(s1)
print(s1[::-1])
for i in range(len(s1)-1, 0, -1):
    print(i)
    res = res + s1[i] + " "

print(res)

# def reverseList(li):
#     start = 0
#     end = len(li) - 1
#     while start < end:
#         li[start], li[end] = li[end], li[start]
#         start += 1
#         end -= 1
#     print(li)
#
# A = [1,2,3,4,5,6]
# reverseList(A)



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
