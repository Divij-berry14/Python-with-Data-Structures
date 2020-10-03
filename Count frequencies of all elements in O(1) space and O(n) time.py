def duplicateElement(arr):
    res = []
    for i in range(len(arr)):
        temp = arr[i]
        if arr[abs(temp)] > 0:
            arr[abs(temp)] *= -1
        else:
            res.append(abs(arr[i]))
        print(arr)
    print(res)

arr = [1, 2, 3, 1, 3, 6, 6, 6]
duplicateElement(arr)