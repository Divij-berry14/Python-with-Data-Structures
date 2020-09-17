class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    while(head is not None):
        print(str(head.data), "-->", end=' ')
        head = head.next
    print("None")
    return 

def length(head):
    count = 0
    while head is not None:
        count = count+1
        head = head.next
    return count

def getDecimalValue(head):
    arr = []
    while head is not None:
        temp = head.data
        arr.append(str(temp))
        head = head.next
    value = "".join(arr)
    res = int(value, 2)
    return res

def inputLL():
    head = None
    tail = None
    inputList = [int(x) for x in input().split()]
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head


head = inputLL()
printLL(head)
print(getDecimalValue(head))
