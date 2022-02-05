class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_ll(head):
    while head is not None:
        print(str(head.data), "->", end="")
        head = head.next
    print("None")
    return head


def length_ll(head):
    count = 0
    while head is not None:
        count = count + 1
        head = head.next
    return count


def insert_at_i(head, i, data):
    if 0 > i > length_ll(head):
        return head
    count = 0
    prev = None
    curr = head

    while count < i:
        prev = curr
        curr = curr.next
        count = count + 1

    new_node = Node(data)

    if prev is not None:
        prev.next = new_node
    else:
        head = new_node

    new_node.next = curr
    return head


def take_input():
    head = None
    input_arr = [int(x) for x in input().split()]
    for curr_data in input_arr:
        if curr_data == -1:
            break
        new_node = Node(curr_data)
        if head is None:
            head = new_node
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    return head


Head = take_input()
print_ll(Head)
Head = insert_at_i(Head, 2, 6)
print_ll(Head)
Head = insert_at_i(Head, 0, 9)
print_ll(Head)
