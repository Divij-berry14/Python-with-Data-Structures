class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def k_reverse(head, n):
    curr = head
    prev = None
    count = 0
    while curr is not None and count < n:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        count += 1
    if temp is not None:
        head.next = k_reverse(temp, n)
    return prev


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
Head = k_reverse(Head, 3)
print_ll(Head)