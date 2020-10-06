def Bubble_Sort(li):
    length = len(li)
    rounds = length-1
    while(rounds > 0):
        for i in range(0, length-1, 1):
            if(li[i] > li[i+1]):
                li[i], li[i+1] = li[i+1], li[i]
            print(li)
        rounds = rounds-1
    for i in li:
        print(i, end=' ')
n = int(input())
li = [int(x) for x in input().split()]
Bubble_Sort(li)

