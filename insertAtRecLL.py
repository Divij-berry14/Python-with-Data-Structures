class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printLL(head):
    while(head is not None):
        print(str(head.data),"->",end='')
        head=head.next
    print("None")
    return

def lengthLL(head):
    count=0
    while(head is not None):
        count=count+1
        head=head.next
    return head

def insertAtRecLL(head,i,data):
    if i<0:
        return head
    
    if i==0:
        newNode=Node(data)
        newNode.next=head
        return newNode
    
    if head is None:
        return None
    
    smallhead=insertAtRecLL(head.next,i-1,data)
    head.next=smallhead
    return head

def takeInput():
    inputList=[int(ele) for ele in input().split()]
    head=None
    tail=None
    for currData in inputList:
        if currData==-1:
            break
        newNode=Node(currData)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
            
    return head

head = takeInput()
printLL(head)
head=insertAtRecLL(head,2,7)
printLL(head)
head=insertAtRecLL(head,0,9)
printLL(head)


            
    
  
    
    

