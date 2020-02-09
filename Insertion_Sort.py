def Insertion_Sort(li):
    length=len(li)
    for i in range(1,length):
        j=i-1
        temp=li[i]
        while(j>=0 and li[j]>temp):
            li[j+1]=li[j]
            j=j-1
        li[j+1]=temp
    for i in li:
        print(i,end=' ')    
li=[int(x) for x in input().split()]
Insertion_Sort(li)
