# def Selection_Sort(li):
#     length = len(li)
#     for i in range(length-1):
#         minIndex = i
#         for j in range(i+1, length):
#             if(li[minIndex] > li[j]):
#                 minIndex = j
#         li[i], li[minIndex] = li[minIndex], li[i]
#         print(li)
    
def Selection_Sort(li):
    l = len(li)
    for i in range(l):
        minIndex = i
        for j in range(i+1,l):
            if li[minIndex] > li[j]:
                minIndex = j
        li[i], li[minIndex] = li[minIndex], li[i]
    print(li)
#li=[1,3,2,4,0,6,8]
li = [int(x) for x in input().split()]
Selection_Sort(li)
print(li)