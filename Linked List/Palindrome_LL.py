class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printLL(head):
    while head is not None:
        print(str(head.data),"-->",end=' ')
        head=head.next
    print("None")
    return

def check_palindrome(head) :
    if head is None:
        return True
    
    # Storing all elements of LinkedList into a List s
    s = []
    while head is not None:
        s.append(head.data)
        head = head.next
    
    # Now simply check whether elements of 's' are in palindrome or not
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True



def inputLL():
    head=None
    tail=None
    inputlist=[int(x) for x in input().split()]
    for currdata in inputlist:
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


head=inputLL()
printLL(head)
res=check_palindrome(head)
print(res)

    
    
    
    