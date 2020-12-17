#nlogn
def binarySearch(arr, low, high, x):
    if low <= high:
        mid = low + (high - low)//2
        if arr[mid] == x:
            return arr[mid]
        elif x > arr[mid]:
            return binarySearch(arr, mid+1, high, x)
        else:
            return binarySearch(arr, low, mid-1, x)

def countpairs(arr, k):
    n = len(arr)
    arr.sort()
    count = 0
    for i in range(n):
        if binarySearch(arr, i+1, n-1, arr[i]+k):
            print(arr[i])
            count += 1
    return count

arr = [1,4,5,3,2]
k = 3
print(countpairs(arr, k))