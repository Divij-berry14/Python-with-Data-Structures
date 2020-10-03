# def printfrequency(arr, n):
#     # Subtract 1 from every element so that
#     # the elements become in range from 0 to n-1
#     res=[]
#     for j in range(n):
#         arr[j] = arr[j] - 1
#
#     # Use every element arr[i] as index
#     # and add 'n' to element present at
#     # arr[i]%n to keep track of count of
#     # occurrences of arr[i]
#     for i in range(n):
#         arr[arr[i] % n] = arr[arr[i] % n] + n
#
#         # To print counts, simply print the
#     # number of times n was added at index
#     # corresponding to every element
#     print(arr)
#     for i in range(n):
#         print(i + 1, "->", arr[i] // n)
#
#     print("Duplicates elements are:")
#     for i in range(n):
#         if arr[i] // n > 1:
#             res.append(i + 1)
#     print(res)
#     # Driver code
#
#



# arr = [4,3,2,7,8,2,3,1,3]
# n = len(arr)
# printfrequency(arr, n)

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?

#In this what we are doing is that, we are taking the particular value of the arr and treated them an an index. And then
# we are going to that index and making it negative. If some other element again get to that position and see if it is negative
# then it means it is already visited by some element means the number is occuring twice.
def DuplicateElement(arr):
    res = []
    n = len(arr)
    for i in arr:
        i = abs(i)
        if arr[i-1] > 0:
            arr[i-1] *= -1
        else:
            res.append(i)
    print(res)

arr = [4,3,2,7,8,2,3,1]
DuplicateElement(arr)

