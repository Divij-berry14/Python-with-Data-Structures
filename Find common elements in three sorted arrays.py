def findCommon(ar1, ar2, ar3):
    n1 = len(ar1)
    n2 = len(ar2)
    n3 = len(ar3)

    i, j, k = 0, 0, 0

    while (i < n1 and j < n2 and k < n3):

        if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
            print(ar1[i])
            i += 1
            j += 1
            k += 1

        # x < y
        elif ar1[i] < ar2[j]:
            i += 1
            print(ar1[i])

        # y < z
        elif ar2[j] < ar3[k]:
            j += 1
            print(ar2[j])

        else:
            k += 1
            print(ar3[k])

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
findCommon(ar1, ar2, ar3)

def Union(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    i = 0
    j = 0
    while(i < m and j < n):
        if arr1[i] < arr2[j]:
            print(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            print(arr2[j])
            j += 1
        else:
            print(arr2[j])
            i += 1
            j += 1
    while i < m:
        print(arr1[i])
        i += 1
    while j < n:
        print(arr2[j])
        j += 1

def Intersection(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    i = 0
    j = 0
    while(i < m and j < n):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            print(arr2[j])
            i += 1
            j += 1


# arr1 = [1, 2, 4, 5, 6]
# arr2 = [2, 3, 5, 7]
# Union(arr1, arr2)
# print()
# Intersection(arr1, arr2)

