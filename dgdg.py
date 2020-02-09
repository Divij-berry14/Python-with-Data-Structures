def min1(li):
    l=len(li)
    li.sort()
    li1=[]
    for i in range(l):
        j=i+1
        for j in range(l-1):
            if(li[i]%2==0):
                temp=li[i]//2
                diff=abs(temp-li[j])
                li1.append(diff)
    m=min(li1)
    return m


li=list(map(int, input.split()))
out=min1(li)
print(out)