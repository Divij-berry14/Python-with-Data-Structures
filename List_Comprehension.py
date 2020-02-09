# LI_NEW=[OUTPUT FOR  CONDITIONS]
#li1=[1,2,3,6]
#li2=[1, 45,6,7]
#li_intersect=[i for i in li1 for j in li2 if i==j]
#print(li_intersect)
#li3=[1,2,3,4,8]
#li_inter=[ele**2 if ele%2==0 else ele for ele in li3]
#print(li_inter)
#li=["Divij", "Berry","Jimmy"]
#li_new=[[s for s in ele]for ele in li]
#print(li_new)


#HOW TO TAKE INPUT OF 2-D LIST METHOD-1
str=input().split()
print(str)
n,m=int(str[0]),int(str[1])
li=[[int(j) for j in input().split()]for i in range(n)]
print(li)

#HOW TO TAKE INPUT OF 2-D LIST METHOD-2
str=input().split()
n,m=int(str[0]),int(str[1])
b=input().split()
li=[[int(b[m*i+j]) for j in range(m)]for i in range(n)]
print(li)

#PRINT 2-D JAGGED lIST
#li=[[1,2,3,4],[2,4],[4,5,6],[10]]
#n=3 
#for row in li:
#    for ele in row:
#        print(ele,end=' ')
#    print()
#
#li=[[1,2,3,4],[2,4],[4,5,6],[10]]
#for row in li:
#    output=' '.join(str(ele) for ele in row)
#    print(output)