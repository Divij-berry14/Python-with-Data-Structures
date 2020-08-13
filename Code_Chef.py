class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def LengthLL(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def LenghtLLRec(head):
    if head is None:
        return 0
    p=LenghtLLRec(head.next)+1
    return p

def InsertNodeLL(head,data,i):
    if i < 0 or i > LenghtLLRec(head):
        return head
    if data == None:
        return head
    newNode=Node(data)
    curr = head
    prev = None
    count = 0
    while(curr is not None):
        if count == i:
            pass


def DeleteNode(head,i):
    if i < 0 or i > LengthLL(head):
        return head
    curr = head
    prev = None
    count = 0
    if i == 0:
        head = curr.next
        curr = None
        return head
    while curr is not None:
        if count == i:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next
        count = count+1
    return head

def printLL(head):
    count = 0
    while head is not None:
        print(head.data,"->",end=" ")
        head = head.next
    print("None")


def InputLL():
    Inputli = [int(x) for x in input().split()]
    head = None
    tail = None
    for currdata in Inputli:
        if currdata == -1:
            break
        node = Node(currdata)
        if head == None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node

    return head

head = InputLL()
printLL(head)
# head = DeleteNode(head,3)
# printLL(head)
print(LenghtLLRec(head))

