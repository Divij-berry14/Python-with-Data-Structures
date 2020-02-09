import math
string=input()
l=len(string)
square_root=math.sqrt(l)
column=math.ceil(square_root)
row=math.floor(square_root)
if(row * column):
    pass
else:
    row=row+1
    if(column * row >= l):
        pass
#for i in range(row):
#    for j in range(column):
#        li[i][j]=string[j]
#print(li)

#li=[[string[j] for j in range(column)]for i in range(row)]
for i in range(column):
    print(string[i::column],end= ' ')
    
#print(l)
#print(square_root)
#print(column)
#print(row)
#


