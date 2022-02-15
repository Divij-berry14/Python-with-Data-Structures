class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length_ll(head):
    count = 0
    while head is not None:
        head = head.next
        count += 1
    return count


def append_last_n_to_first(head, n):
    count = length_ll(head)
    curr = head
    prev = None
    temp1 = head
    while curr is not None:
        curr = curr.next
    temp2 = count - n
    temp3 = 0
    while temp1 is not None and temp3 != temp2:
        prev = temp1
        temp1 = temp1.next
        temp3 += 1
    prev.next = None
    head1 = temp1
    while temp1.next is not None:
        temp1 = temp1.next
    temp1.next = head
    return head1


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
Head = append_last_n_to_first(Head, 5)
print_ll(Head)
