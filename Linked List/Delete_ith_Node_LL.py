class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_ll(head):
    while head is not None:
        print(str(head.data), "-->", end=" ")
        head = head.next
    return


def length_ll(head):
    count = 0
    while head is not None:
        head = head.next
        count = count+1
    return count


def delete_node(head, i):
    if i < 0 or i >= length_ll(head):
        return head
    curr = head
    prev = None
    count = 0
    while count < i:
        prev = curr
        curr = curr.next
        count += 1
    if i is 0:
        head = curr.next
        return head
    else:
        prev.next = curr.next
    return head


def take_input():
    input_list = [int(i) for i in input().split()]
    head = None
    tail = None
    for currData in input_list:
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
print_ll(Head)
in_var = int(input())
Head = delete_node(Head, in_var)
print_ll(Head)