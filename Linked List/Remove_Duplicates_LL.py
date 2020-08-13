class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def eliminate_duplicate(head):
    curr=head
    while(curr is not None and curr.next is not None):
        if(curr.data==curr.next.data):
            new=curr.next.next
            curr.next=None
            curr.next=new
        else:
            curr=curr.next
            
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
l = eliminate_duplicate(l)
printll(l)