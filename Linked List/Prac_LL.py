class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def printLL(head):
    while(head is not None):
        print(str(head.data),"-->",end=' ')
        head=head.next
    print("None")
    return 


def length(head):
    count=0
    while head is not None:
        count=count+1
        head=head.next
    return count

def insert_ith_LL(head,i):
    count=0
    curr=head
    while curr is not None:
        if count==i:
            print(str(curr.data),end=' ')
            break
        else:
            count=count+1
            curr=curr.next

def del_ith_rec(head,i):
    curr=head
    if head is None:
        return None
    if i==0:
        p=curr.next
        return p
    
    
    smallhead=del_ith_rec(head.next,i-1)
    head.next=smallhead
    return head
        


def inputLL():
    head=None
    tail=None
    inputList=[int(x) for x in input().split()]
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


head=inputLL()
printLL(head)
insert_ith_LL(head,3)
printLL(head)
del_ith_rec(head,2)
printLL(head)