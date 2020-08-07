import copy
li1=[[1,2],3,4]
li2=copy.copy(li1)
print(li1)
print(li2)
li2.append(5)
print(li1)
print(li2)
li2[0][1]="a"
print(li1)
print(li2)
li2[0].append("new")
print(li1)
print(li2)