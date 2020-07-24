def qu(customers):
    l = len(customers)
    d = {}
    li = []
    for i in customers:
        d[i] = d.get(i, 0) + 1
    for j in d:
        per = (d[j] / l) * 100
        if per > 5:
            li.append(j)
    li.sort()
    return li

customers=["Omega","Alpha","Omega","Alpha","Omega","Alpha","Beta"]
res=qu(customers)
print(res)



