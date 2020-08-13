class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def append_LinkedList(head,n) :
    #  Given a linked list and an integer n, append the last n elements of the LL
    #  to front. 
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    curr = head
    temp1 = head
    prev = None
    count = 0
    while curr:
        count+=1
        curr=curr.next
    temp2 = count - n
    res = 0
    while temp1 and res!=temp2:
        prev = temp1
        temp1 = temp1.next
        res+=1
    prev.next = None
    temp3 = temp1
    while temp3.next!=None:
        temp3 = temp3.next
    temp3.next = head
    return temp1

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
i=int(input())
l = append_LinkedList(l, i)
printll(l)