#This problem was asked in Amazon, Zoho, Paytm and MakeMyTrip.
#
#Given an array, containing only 0 and 1 as its elements. The elements are kept in random order. You have to sort the array. The constraints are:
#1. You cannot count or add the elements of arrays.
#2. You cannot use an extra array. 
#
#For example, if the input array is: [0, 1, 1, 0, 1, 1], then the output array must be: [0, 0, 1, 1, 1, 1]
#Expected Complexity: Try doing it in O(n) time complexity and O(1) space complexity. Here, n is the size of the array.
#
#Input format :
#Line 1: Integer N (Array Size)
#Line 2: Array elements (separated by space)
#
#Output format :
#Sorted array elements
#Constraints :
#1 <= N <= 10^6
#
#Sample Input :
#7
#0 1 1 0 1 0 1
#
#Sample Output :
#0 0 0 1 1 1 1

# Input- 1 1 0 1 0 1 0 0 0 0 1 1 1 1 1 1 1 1 0 1 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 0 0  1 1 1 1 0 0 1 1 0 1 1 0 0 1 1 1 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 1 1 0 1 0 1 0 1 0 0 1 0 1 1 0 1 0 1 1 0 1 1 1 0 0 0 0 1 1 1 1 1 0 0 1 0 1 0 1 0 0 1 0 0 1 1 0 1 1 1 1 0 1 0 1 1 1 0 0 0 1 0 0 0 0 0 0 1 0 1 0 1 0 1 0 0 1 1 0 1 0


n=int(input())
li=[int(x) for x in input().split()]
l=len(li)
i=0
j=l-1
while(j>i):
    if li[i]>li[j]:
        li[i],li[j]=li[j],li[i]
        i=i+1
        j=j-1
    else:
        if li[i]==0 and li[j]==1:
            i=i+1
            j=j-1
        elif li[i]==1 and li[j]==1:
            j=j-1
        elif li[i]==0 and li[j]==0:
            i=i+1

print()          
print(*li)
    