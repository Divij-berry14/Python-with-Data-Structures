#Line 1 : Integer N (Array Size)
#Line 2 : Array elements (separated by space)
#Line 3 : Integer x
#Line 1 : Triplet 1 elements (separated by space)
#Line 2 : Triplet 3 elements (separated by space)
#Line 3 : and so on
#7
#1 2 3 4 5 6 7 
#12
#1 4 7
#1 5 6
#2 3 7
#2 4 6
#3 4 5
m=int(input())
li=[int(x) for x in input().split()]
li.sort()
sum=int(input())

for i in range(m):
    for j in range(i+1,m):
        for k in range(j+1,m):
          if li[i]+li[j]+li[k]==sum:
            print(li[i],li[j],li[k])