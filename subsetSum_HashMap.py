#10  95 -97 -387 -435 -5 -70 897 127 23 284

#6 3 -1 2 -4 3 1 -2 20

def subsetSum(l):
    n=len(l)
    m = {l[0] : 0}
    sum=[0]*n
    sum[0]=l[0]
    start=-1
    end=-2
    if sum[0]==0:
        start,end=0,0
    for i in range(1,n):
        sum[i]=sum[i-1]+l[i]
        if sum[i]==0:
            start,end=0,i
        elif sum[i] in m:
            if i-m[sum[i]]>end-start+1:
                start,end=m[sum[i]]+1,i
        else:
            m[sum[i]]=i
    return start,end

n=int(input())
l=list(int(i) for i in input().strip().split(' '))
start,end= subsetSum(l)
print(end-start+1)