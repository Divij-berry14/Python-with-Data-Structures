class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def eliminate_duplicate(head):
    curr = head
    while curr is not None and curr.next is not None:
        if curr.data == curr.next.data:
            new = curr.next.next
            curr.next = None
            curr.next = new
        else:
            curr = curr.next

    return head


def print_ll(head):
    while head is not None:
        print(head.data, "->", end="")
        head = head.next
    print("None")


def input_ll():
    li_val = [int(i) for i in input().split()]
    head = None
    tail = None
    for curr_val in li_val:
        if curr_val is -1:
            break
        new_node = Node(curr_val)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head


Head = input_ll()
print_ll(Head)
Head = eliminate_duplicate(Head)
print_ll(Head)