class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    
a = Node(12)
b = Node(17)
a.next = b
print(a)
print(a.next)
print(a.data)
print(a.next.data)
print(b)
print(b.next)
print(b.data)    

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next



node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
printLL(node2)




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def ithNode(head, i):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    count=0
    curr=head
    while(curr is not None):
        if(count<i and curr!=None):
            curr=curr.next
            count=count+1
    return curr
        
        
        

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

        
        
        
        
        