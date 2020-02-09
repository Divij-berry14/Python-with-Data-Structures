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