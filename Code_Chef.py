t=int(input())
for i in range(t):
    li1=[]
    age=[]
    cost=[]
    dict={}
    li=[int(x) for x in input().split()]
    age=li[:3]
    cost=li[3:]
    #age.sort()
    dict[age[0]]=cost[0]
    dict[age[1]]=cost[1]
    dict[age[2]]=cost[2]
    for j in sorted(dict.keys()):
        print((j,dict[j]),end=' ')
#        if(dict[j]==max(dict)):
#            print("NOT FAIR")
            
        #print(dict)
    
#    li1.extend(age)
#    li1.extend(cost)
#    print(li1)
#    print(li)
#    if(li==li1):
#        print("FAIR")
#    else:
#        print("NOT FAIR")
#    if(age[0]==age[1]==age[2] and cost[0]==cost[1]==cost[2]):
#        print("FAIR")
#    else:
#        print("NOT FAIR")
#    if(age[1]==age[2] and cost[1]==cost[2]):
#        if(age[0]>age[1] and cost[0]>cost[1]):
#            print("FAIR")
#        else:
#            print("NOT FAIR")
#    if(age[0]==age[1] and cost[0]==cost[1]):
#        if(age[2]>age[1] and cost[2]>cost[1]):
#            print("FAIR")
#        else:
#            print("NOT FAIR")
#    if(age[0]==age[2] and cost[0]==cost[2]):
#        if(age[1]>age[2] and cost[1]>cost[2]):
#                print("FAIR")
#        else:
#            print("NOT FAIR")
    
        