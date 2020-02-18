# t=int(input())
# for i in range(t):
# 	n = int(input())
# 	li = [int(x) for x in input().split()]
# 	l=len(li)
# 	zero=li.count(0)
# 	one=li.count(1)
# 	zeros=1
# 	ones=1
# 	length = l
# 	for i in range(l):
# 		if zero > (length//2):
# 			print(length)
# 		if i%2==0:
# 			zeros+=1
# 		else:
# 			ones+=1



# n = int(input())
# tax1 = 12500
# tax2 = 25000
# tax3 = 37500
# tax4 = 50000
# tax5 = 62500
# final_income=0
# for i in range(n):
# 	income = int(input())
# 	if income <= 250000:
# 		print(income)
# 	if income>=250000 and income<=500000:
# 		tax=abs(income-250000)*0.05
# 		final_income=income-tax
# 		print(int(final_income))
# 	if income>=500000 and income<=750000:
# 		tax=abs(income-500000)*0.1+tax1
# 		final_income=income-tax
# 		print(int(final_income))
# 	if income>=750000 and income<=1000000:
# 		tax=((income-750000)*0.15)+tax2+tax1
# 		print(int(income-tax))
# 	if income>1000000 and income<1250000:
# 		tax=abs(income-1000000)*0.2+tax3+tax2+tax1
# 		final_income=income-tax
# 		print(int(final_income))
# 	if income>1250000 and income<1500000:
# 		tax=abs(income-1250000)*0.25+tax4+tax1+tax2+tax3
# 		final_income=income-tax
# 		print(int(final_income))
# 	if income>1500000:
# 		tax=abs(income-1500000)*0.3+tax1+tax2+tax3+tax4+tax5
# 		final_income=income-tax
# 		print(int(final_income))

# t = int(input())
# for i in range(t):
# 	n = int(input())
# 	s1 = [int(x) for x in input().split()]
# 	s2 = [int(y) for y in input().split()]
# 	s1.sort()
# 	s2.sort()
# 	max = 0
# 	j=0
# 	while(j<len(s1)):
# 		if s1[j]>s2[j]:
# 			max=max+s2[j]
# 			print(max)
# 		else:
# 			max=max+s1[j]
# 			print(max)
# 		j=j+1
# 	print(max)




