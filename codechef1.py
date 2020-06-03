import math
def kClosest(points, K):
    points.sort()
    print(points)
    li = []
    s = 0
    min=-1
    if k==1:
        li.append(points[0])
        return li
    a=points[0][0]**2+points[0][1]**2
    min=math.sqrt(a)
    s=s+1
    li.append(points[0])
    for i in range(1,len(points)):
        a = points[i][0]**2 + points[i][1]**2
        # print(a)
        if math.sqrt(a) <= min and s<K:
            li.append(points[i])
            s = s + 1
            if s == K:
                break
            else:
                min=a
    del points
    return li

li=[[-5,4],[-6,-2],[4,8]]
k=2
res=kClosest(li,k)
print(res)