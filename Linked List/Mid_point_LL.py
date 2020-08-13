class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def print_LL(head):
    while(head is not None):
        print(str(head.data)," -->",end=' ')
        head=head.next
    print("None")
    return

def length(head):
    count=0
    while(head is not None):
        count=count+1
        head=head.next
    return count

def mid_element_LL(head):
    slow=head
    fast=head
    while fast.next!=None and fast.next.next!=None:
        slow=slow.next
        fast=fast.next.next
    print(str(slow.data))
    return

def input_LL():
    head=None
    tail=None
    input_list=[int(x) for x in input().split()]
    for currdata in input_list:
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

head=input_LL()
print_LL(head)
mid_element_LL(head)

