#5
#0 3 0 2 0

#3 2 0 0 0

n=int(input())
count=0
li1=[]
li=[int(x) for x in input().split()]
length=len(li)
i=0
while(i<length):
    if(li[i]==0):
        li.remove(li[i])
        length=length-1
        count=count+1
    i=i+1
    

while(count>0):
    li.append("0")
    count=count-1
    
for j in li:
    print(j,end=' ')
        
               #OR 
    
n = int(input())
list_1 = [int(x) for x in input().split()]
list_2 = []
count_zeros = 0
for temp in list_1 :
	if temp == 0:
		count_zeros += 1
	else:
		list_2.append(str(temp))

for x in range(0, count_zeros):
	list_2.append("0")

print(" ".join(list_2))

#con
