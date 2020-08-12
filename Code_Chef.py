def hIndex(citations):
    n = len(citations)
    l, r = 0, n - 1
    while (l <= r):
        mid = int(l + (r - l) / 2)
        print("mid",mid)
        if citations[mid] < n - mid:
            l = mid + 1
            print("l",l)
        else:
            r = mid - 1
            print("r",r)
    return n - l

li = [int(x) for x in input().split()]
print(hIndex(li))



