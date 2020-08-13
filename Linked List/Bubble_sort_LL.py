class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def count(head):
    if head is None:
        return -1
    i=1
    while head.next is not None:
        head=head.next
        i+=1
   
    return i
       
def bubbleSortLL(head) :
    n=count(head)
    for i in range(n):
        prev=None
        x=None
        if head.data>head.next.data:
            x=head.next
            head.next=x.next
            x.next=head
            head=x
        c=head
        while c is not None and c.next is not None:
            next=c.next
            if c==head.next:
                prev=head
            if c.data>next.data:
                prev.next=c.next
                c.next=next.next
                next.next=c
            else:
                c=c.next
           
            if prev is not None:
                prev=prev.next
           
    return head
           
       
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = bubbleSortLL(l)
printll(l)