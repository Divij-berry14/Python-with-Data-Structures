class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def ithNode(head, i):
    count=0
    curr=head
    while curr is not None:
        if count == i:
            return curr
        count += 1
        curr = curr.next
        
        
        

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
node = ithNode(l, i)
if node:
    print(node.data)

        