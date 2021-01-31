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
    p = LenghtLLRec(head.next)+1
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
    p = InsertNodeLL(head.next,data,i-1)
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

def ReverseLL(head):
    if head is None:
        return None
    curr = head
    prev = None
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def PalindromeLL(head):
    if head is None:
        return True
    s = []
    while head is not None:
        s.append(head.data)
        head = head.next
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left = left + 1
        right = right - 1
    return True

def ReverseLLII(head, m, n):
    start, prev, node, count = None, None, head, 1
    while count <= n:
        nextNode = node.next
        if count == m:
            start = prev
        elif count > m:
            node.next = prev
        prev, node = node, nextNode
        count += 1

    if start:
        start.next.next = node
        start.next = prev
    else:
        head.next = node
        head = prev
    return head
    # if head is None:
    #     return None
    # curr1 = head
    # prev = None
    # i = 1
    # j = m - 1
    # while curr1 is not None:
    #     if i == n:
    #         tempHead = curr1
    #         break
    #     else:
    #         curr1 = curr1.next
    #         i += 1
    #
    # while tempHead is not None:
    #     if j > 0:
    #         temp = tempHead.next
    #         tempHead.next = prev
    #         prev = tempHead
    #         tempHead = temp
    #         j -= 1
    # curr1.next = prev
    # return head

def MidElementLL(head):
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    print(str(slow.data))
    return

def merge_two_sorted_arrays(head1,head2):
    if head1 and head2 is None:
        return None
    finalHead = None
    finalTail = None
    if head1. data > head2.data:
        finalHead = head2
        finalTail = head2
        head2 = head2.next
    else:
        finalHead = head1
        finalTail = head1
        head1 = head1.next

    while head1 is not None and head2 is not None:
        if head1.data > head2.data:
            finalTail.next = head2
            finalTail = finalTail.next
            head2 = head2.next
        else:
            finalTail.next = head1
            finalTail = finalTail.next
            head1 = head1.next

    if head1 is not None:
        finalTail.next = head1
    if head2 is not None:
        finalTail.next = head2

    return finalHead

def swapNodes(head, x, y):
    if head is None:
        return None
    if x == y:
        return head
    currX = head
    currY = head
    prevX = None
    prevY = None
    while currX is not None and currX.data != x:
        prevX = currX
        currX = currX.next
    while currY is not None and currY.data != y:
        prevY = currY
        currY = currY.next

    if prevX!=None:
        prevX.next = currY
    else:
        head = currY
    if prevY!=None:
        prevY.next = currX
    else:
        head = currX
    temp = currX.next
    currX.next = currY.next
    currY.next = temp
    return head

def nextLargerNodes(head):
    if head is None:
        return None
    temp = []
    while head is not None:
        temp.append(head.data)
        head = head.next
    res = []
    for i in range(len(temp)):
        j = i+1
        while(j <= len(temp)-1):
            if temp[j] < temp[i]:
                j += 1
            if j == len(temp)-1:
                res.append(0)
            else:
                res.append(temp[j])
                break
    return res

def OddEvenLL(head):
    if head is None:
        return None
    curr = head
    evenHead = None
    evenTail = None
    oddHead = None
    oddTail = None
    while curr is not None:
        if curr.data % 2 ==0:
            if evenHead is None:
                evenHead = curr
                evenTail = curr
            else:
                evenTail.next = curr
                evenTail = curr
        else:
            if oddHead is None:
                oddHead = curr
                oddTail = curr
            else:
                oddTail.next = curr
                oddTail = curr
        curr = curr.next
    if oddHead is None:
        return evenHead
    oddTail.next = evenHead
    evenTail.next = None
    head = oddHead
    return head

def skipMdeleteN(head, m, n):
    if head is None:
        return None
    if m == 0:
        return head
    if n < 0 or m < 0:
        return head
    curr = head
    newHead = None
    while curr is not None:
        for i in range(m-1):
            if curr is None:
                return head
            curr = curr.next
            # print(i)
        prev = curr
        curr = curr.next
        for i in range(n):
            if curr is None:
                return head
            curr = curr.next
        prev.next = curr
    return head

def printLL(head):
    count = 0
    while head is not None:
        print(head.data, "->", end=" ")
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
# head2 =InputLL()
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
# head = RemoveDuplicatesLL(head)
# printLL(head)
# head = ReverseLL(head)
# printLL(head)
# print(PalindromeLL(head))
# head = ReverseLLII(head,2,3)
# printLL(head)
MidElementLL(head)
# head = merge_two_sorted_arrays(head1, head2)
# printLL(head)
# head = OddEvenLL(head)
# printLL(head)
# head = skipMdeleteN(head, 2, 2)
# printLL(head)

