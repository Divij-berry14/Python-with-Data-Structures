class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def mid_point_LL(head):
    slow=head
    fast=head
    while slow.next is not None and fast.next and fast.next.next is not None:
        slow=slow.next
        fast=fast.next.next
    return slow

def merge(head1,head2):
    if head1==None:
        return head2
    if head2==None:
        return head1
    if head1.data<head2.data:
        head=head1
        head1=head1.next
    else:
        head=head2
        head2=head.next
    curr=head
    while head1 is not None and head2 is not None:
        if head1.data<head2.data:
            curr.next=head1
            head1=head1.next
        else:
            curr.next=head2
            head2=head2.next
        curr=curr.next
    if head1 is None:
        curr.next=head2
    if head2 is None:
        curr.next=head1
    return head
        
    
def mergeSort(head):
    if head== None:
        return None
    if head.next is None:
        return head
    mid=mid_point_LL(head)
    head1=head
    head2=mid.next
    mid.next=None
    head1=mergeSort(head1)
    head2=mergeSort(head2)
    head=merge(head1,head2)
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
l = mergeSort(l)
printll(l)