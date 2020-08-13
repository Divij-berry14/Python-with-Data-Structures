class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def print_LL(head):
    while(head is not None):
        print(str(head.data),"-->",end=' ')
        head=head.next
    print("None")
    return head

def merge_two_sorted_arrays(head1,head2):
    finalHead=None
    finalTail=None
    if head1.data > head2.data:
            finalHead=head2
            finalTail=head2
            head2=head2.next
    while head1 is not None and head2 is not None:
        if head1.data > head2.data:
            finalTail.next=head2
            finalTail=finalTail.next
            head2=head2.next
        
        else:
            finalTail.next=head1
            finalTail=finalTail.next
            head1=head1.next
    
    if head1 is not None:
        finalTail.next=head1
    if head2 is not None:
        finalTail.next=head2
    
    return finalHead

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

head1=input_LL()
head2=input_LL()
head=merge_two_sorted_arrays(head1,head2)
print_LL(head)

    
        
    
            
            
            
        
            