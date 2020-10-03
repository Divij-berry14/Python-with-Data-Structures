# def duplicateElement(arr):
#     res = []
#     for i in range(len(arr)):
#         temp = arr[i]
#         if arr[abs(temp)] > 0:
#             arr[abs(temp)] *= -1
#         else:
#             res.append(abs(arr[i]))
#         print(arr)
#     print(res)
#
# arr = [1, 2, 3, 1, 3, 6, 6, 6]
# duplicateElement(arr)



def findCounts(arr, n):

    i = 0
    while i < n:

        if arr[i] <= 0:
            i += 1
            continue
        elementIndex = arr[i] - 1

        if arr[elementIndex] > 0:
            arr[i] = arr[elementIndex]

            arr[elementIndex] = -1
            print(arr)

        else:

            arr[elementIndex] -= 1

            arr[i] = 0
            i += 1
            print(arr)

    print("Below are counts of all elements")
    for i in range(0, n):
        print("%d -> %d" % (i + 1, abs(arr[i])))
    print("")


# Driver program to test above function
arr = [2, 3, 2, 3, 5]
findCounts(arr, len(arr))

# arr1 = [1]
# findCounts(arr1, len(arr1))
#
# arr3 = [4, 4, 4, 4]
# findCounts(arr3, len(arr3))
#
# arr2 = [1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1]
# findCounts(arr2, len(arr2))
#
# arr4 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
# findCounts(arr4, len(arr4))
#
# arr5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# findCounts(arr5, len(arr5))
#
# arr6 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# findCounts(arr6, len(arr6))

# This code is contributed
# by shreyanshi_19


