class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_LL(head):
    while head is not None:
        print(str(head.data),"->",end='')
        head = head.next
    print("None")
    return


def length_LL(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return head


def insert_at_pos_rec(head, i, data):
    if i < 0:
        return head

    if i == 0:
        new_node = Node(data)
        new_node.next = head
        return new_node

    if head is None:
        return None

    small_head = insert_at_pos_rec(head.next, i-1, data)
    head.next = small_head
    return head


def take_input():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData is -1:
            break
        new_node = Node(currData)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
            
    return head


Head = take_input()
print_LL(Head)
Head = insert_at_pos_rec(Head, 2, 7)
print_LL(Head)
Head = insert_at_pos_rec(Head, 0, 9)
print_LL(Head)


            
    
  
    
    

