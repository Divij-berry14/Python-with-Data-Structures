# Problem ID 331 even after odd in a LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def arrange_LinkedList(head):
    curr=head
    Ehead=None
    Etail=None
    Ohead=None
    Otail=None
    while curr is not None:
        if curr.data%2==0:
            if Ehead is None:
                Ehead=curr
                Etail=curr
            else:
                Etail.next=curr
                Etail=curr
        else:
            if Ohead is None:
                Ohead=curr
                Otail=curr
            else:
                Otail.next=curr
                Otail=curr
        #curr.next=None
        curr=curr.next
    if Ohead is None:
        return Ehead
    Otail.next=Ehead
    return Ohead

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


# MAIN
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = arrange_LinkedList(l)
printll(l)
