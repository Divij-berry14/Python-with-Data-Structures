class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printLL(head):
    while head is not None:
        print(str(head.data),"-->",end=" ")
        head=head.next
    return

def length(head):
    count=0
    while head is not None:
        head=head.next
        count=count+1
    return count

def deleteNode(head, i):
    if i<0 or i>=length(head):
        return head
    curr = head 
    prev=None
    count=0
    if  i==0:
        head = curr.next
        curr = None
        return head
    while(curr is not None):
        if count==i: 
            break 
        prev = curr 
        curr = curr.next 
        count=count+1
    prev.next = curr.next 
    #curr=None
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
i=int(input())
head=deleteNode(head,i)
printLL(head)