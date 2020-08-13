class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    

def print_LL(head):
    while(head is not None):
        print(str(head.data),"-->",end=' ')
        head=head.next
    print("None")
    return

def Linear_Search_LL_rec(head,n):
    if head is None:
        return -1
    
    if head.data==n:
        return 0
    
    result=Linear_Search_LL_rec(head.next,n)
    if result==-1:
        return -1
    return result+1

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
n=int(input())
pos=Linear_Search_LL_rec(head,n)
print(pos)    