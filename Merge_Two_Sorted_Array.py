def Merge_Two_Sorted_Array(li1,li2):
    li3=[]
    i=0
    j=0
    while i<len(li1) and j<len(li2):
        if(li1[i]<li2[j]):
          li3.append(li1[i])
          i=i+1
        else:
          li3.append(li2[j])
          j=j+1
    while(i<len(li1)):
        li3.append(li1[i])
        i=i+1
    while(j<len(li2)):
        li3.append(li2[j])
        j=j+1
        
    for m in li3:
        print(m,end=' ')
n1=int(input())
li1=[int(x) for x in input().split()]
n2=int(input())
li2=[int(y) for y in input().split()]
Merge_Two_Sorted_Array(li1,li2)

def Non_Decreasing(li):
    length=len(li)
    count=0
    count1=0
    if(li[0]>li[1]):
        i=0
    else:
        i=1
    while(i<length-1):
        if(li[i]<=li[i+1]):
            count=count+1
            i=i+1
        else:
            if(count1<2):
                li[i]=li[i-1]+1
                count1=count1+1
                print(li)
                i=0
            else:
                print("False")
                break
                
    print(li)
    print(count)
    if(count==length):
        print("True")
    #if(count==length+1)

def Non_Decreasing(li):
    length=len(li)
    found_count=0
    if(li[2]<li[0]):
        if(li[1]<li[0] or li[1]>li[0]):
            return False
    for i in range(1,length-1):
        if(li[i-1]>li[i]):
            found_count+=1
    
    if(found_count>1):
        return False
    else:
        return True

#n=int(input())
li=[int(x) for x in input().split()]
result=Non_Decreasing(li)
print(result)

