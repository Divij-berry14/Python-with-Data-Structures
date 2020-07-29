# def countTriplets(arr, r):
#     l = len(arr)
#     count = 0
#     m = {}
#     for i in arr:
#         m[i] = m.get(i, 0)+1
#     for num in arr:
#         temp=num*r
#         if temp in m and temp*r in m:
#             count=count+m[temp]*m[temp*r]
#     return count
def countTriplets(arr, r):
    count = 0
    dict = {}
    dictPairs = {}

    for i in reversed(arr):
        if i*r in dictPairs:
            count += dictPairs[i*r]
            print("count",count)
        if i*r in dict:
            dictPairs[i] = dictPairs.get(i, 0) + dict[i*r]
            print("dictP",dictPairs)

        dict[i] = dict.get(i, 0) + 1
        print("dict",dict)

    return count

# arr=[int(x) for x in input().split()]
arr=[1,2,1,2,4]
res=countTriplets(arr, 2)
print(res)