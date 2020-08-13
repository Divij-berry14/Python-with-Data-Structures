class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    while(head is not None):
        print(str(head.data),"-->",end=' ')
        head=head.next
    print("None")
    return 

def reverse_LL_rec(head):
    if head is None:
        return
    reverse_LL_rec(head.next)
    print(head.data, end=' ')
#    
def reverse_LL(head):
    prev=None
    curr=head
    while(curr is not None):
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    head=prev
    return head

def reverse_LL2_rec(head):
    if head is None or head.next is None:
        return head
    
    smallhead=reverse_LL2_rec(head.next)
    curr=smallhead
    while curr.next is not None:
        curr=curr.next
    curr.next=head
    head.next=None
    return smallhead

def reverse_LL3_rec_Optimized(head):
    
    if head is None or head.next is None:
        return head,head
    smallhead,smalltail=reverse_LL3_rec_Optimized(head.next)
    smalltail.next=head
    head.next=None
    return smallhead,head

def reverse_LL4_rec_Optimized(head):
    
    if head is None or head.next is None:
        return head
    smallhead=reverse_LL4_rec_Optimized(head.next)
    tail=head.next
    tail.next=head
    head.next=None
    return smallhead


def inputLL():
    head=None
    tail=None
    inputlist=[int(x) for x in input().split()]
    for currdata in inputlist:
        if currdata==-1:
            break
        newNode=Node(currdata)
        if head is None:
            head=newNode
            tail=head
        else:
            tail.next=newNode
            tail=newNode
    return head

head=inputLL()
printLL(head)
reverse_LL_rec(head)
printLL(head)
head=reverse_LL2_rec(head)
printLL(head)
head=reverse_LL(head)
printLL(head)
head,tail=reverse_LL3_rec_Optimized(head)
printLL(head)
head=reverse_LL4_rec_Optimized(head)
printLL(head)


