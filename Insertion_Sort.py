# def InsertionSort(li):
#     length = len(li)
#     for i in range(1, length):
#         j = i - 1
#         temp = li[i]
#         while j >= 0 and li[j] > temp:
#             li[j+1] = li[j]
#             j = j - 1
#             print(j, li)
#         li[j+1] = temp
#         print(li)

def InsertionSort(li):
    l = len(li)
    for i in range(1, l):
        j = i - 1
        temp = li[i]
        while(j>=0 and li[j] > temp):
            li[j+1] = li[j]
            j = j - 1
            print(li, j)
        li[j+1] = temp
        print(li)
    print(li)

li = [int(x) for x in input().split()]
InsertionSort(li)
print(li)
