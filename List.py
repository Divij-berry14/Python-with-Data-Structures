## CREATE A LIST
#li=[1,3,3,4,5]
#print((li))
#
#li1=[1,2,"Divij",3.4,5.6]
#print(li1)
#
##ACCESS AND CHANGE ELEMENTS IN THE LIST
#li1[3]="Berry"
#print(li1)
#
## SLICING OF A LIST
#print(li1[1:3])
#print(li1[1:])
#
## INSERT AND APPEND ELEMENTS IN THE LIST
#li1.append("Life")
#print(li1)
#li1.insert(1,"?")
#print(li1)
#li1.insert(7,"FindOut")
#print(li1)
#
##append list in a list
#li1.append([9,10,11])
#print(li1)
#
## WITH EXTEND FUNCTION WE CAN APPEND MULTIPLE ELEMENTS INDIVIDUALLY,
#li1.extend([9,10,11])
#print(li1)
#
## REMOVING ELEMENTS FROM THE LIST
#li1=[1,2,4,5,6,6,7,4]
#li1.append(2)
#print(li1)
#li1.remove(2)   # REMOVE WILL DELETE THE ELEMENT FROM THE STARTING OF THE LIST
#print(li1)
#
# POP WILL DELETE THE ELEMENT AT THE PARTICULAR INDEX 
#li1=[1,2,4,5,6,6,7,4]
#li1.insert(2,2)
#print(li1)
#li1.pop()   # HERE NO INDEX IS MENTIONED, THUS DELETING THE ELEMENT FROM THE LAST
#print(li1)
#li1.pop(3)
#print(li1)
#print(len(li1))
#
## LIST ACTUALLY STORES REFRENCES OF ELEMENTS
## ALL REFRENCES ARE STORED CONTINOUSLY
## IN LIST CONCEPT OF RESIZING IS DONE FOR STORING ELEMENTS
#
#
## LOOP IN LIST
#
#li2=[1,2,3,"Divij",'Berry']
#for i in range((len(li2))):
#    print(li2[i])
#    
#for i in range(2,len(li2)):
#    print(li2[i])
#
#for ele in li2:
#    print(ele)
#
#for ele in li2[3:]:
#    print(ele)
#
## NEGATIVE INDEXING 
#li3=[1,2,3,4,5,6,7,8,9]
#print(li3[2])
#print(li3[4])
#print(li3[5])
#print(li3[-1])     # -1 MEANS LIST IS STARTING FROM THE LAST ELEMENT
#print(li3[-6])
#print(li3[-8])
#
#
##SEQUENCING LIST   --->> LI[ START : END-1 : STEP ]
#li4=[1,2,3,4,5,6]
#print(li4[1:6:1])    #LI[ START=0 : END=5 : 1]  PRINT LIST FROM 1 TO 5
#print(li4[1:5:1]) 
#print(li4[1:6:2])    
#print(li4[1:5:2])
#print(li4[1:3:2])
#print(li4[2:6:2])
#print(li4[1:6:3])
#print(li4[2:6:3])
#print(li4[0:6:1])
#print(li4[0:6:2])
#
#print(li4[1:])      # HERE START=0 : END=LENGTH OF THE LIST : STEP=1
#print(li4[1::2])
#print(li4[2::2])
#print(li4[0::2])
#
#print(li4[:6])      # START=0 : END= END-1 : STEP=1 
#print(li4[:4])
#
#
##INPUT A LIST
##LINE SEPERATED INPUT
li5=[]
n=int(input())
for i in range(n):
    curr=int(input())
    li5.append(curr)
print(li5)
for ele in li5:
    print(ele)
#
#
## SPACE SEPARTED INPUT
#str=input()  # this will print 1 2 3 4 5 as a string= '1 2 3 4 5'
#print(str)
#str_split=str.split(' ')  # split function separtes based upon the delimentor. 
#print(str_split)          #It will split the str in parts of the list as a string
#                          # ['1', '2' , '3', '4', '5']
#str_split=str.split()     # split automatically according to the space
#print(str_split)
#
#li6=[]
#for ele in str_split:
#    li6.append(int(ele))
#print(li6)
#
#li7=[int(x) for x in input().split()]   # MEANS INPUT- 1 2 3 4 5 6
#print(li7)                             #  FIRST CONVERT TO THIS- ['1', '2','3','4','5','6']
##                                         ANSWER - [1,2,3,4,5,6]
#    
#
#n=input()
#li8=[int(x) for x in input().split()]
#print(li8)
#for ele in li8:
#    print(ele)
#
#
#
#                                       