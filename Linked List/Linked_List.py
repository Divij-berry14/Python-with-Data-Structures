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
    if i == 0:
        newNode.next=head
        head = newNode
        curr = None
    while(curr is not None):
        if count == i:
            prev.next = newNode
            newNode.next = curr
            break
        prev = curr
        curr = curr.next
        count += 1
    return head

def InputNodeRec(head,data,i):
    if head is None:
        return None
    if i == 0:
        newNode = Node(data)
        newNode.next = head
        p = newNode
        return p
    p =  InsertNodeLL(head.next,data,i-1)
    head.next = p
    return head

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

def AppendLastToFirst(head,n):
    if head is None:
        return None
    curr = head
    prev = None
    length = LenghtLLRec(head)
    count = 1
    while curr is not None:
        if count == n:
            temp1 = prev.next
            prev.next = None
        prev = curr
        curr = curr.next
        count += 1
    curr = head
    curr1 = temp1
    while curr1.next is not None:
        curr1 = curr1.next
    curr1.next = curr
    return temp1

def RemoveDuplicatesLL(head):
    if head is None:
        return None
    curr = head
    while curr is not None and curr.next is not None:
        if curr.data == curr.next.data:
            # curr.next = None
            curr.next = curr.next.next
        else:
            curr = curr.next
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
# print(LenghtLLRec(head))
# head = InsertNodeLL(head, 9, 5)
# printLL(head)
# head = InputNodeRec(head, 9, 3)
# printLL(head)
# head = AppendLastToFirst(head,4)
# printLL(head)
head = RemoveDuplicatesLL(head)
printLL(head)