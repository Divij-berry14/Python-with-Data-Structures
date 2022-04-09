class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_ll(head):
    curr = head
    prev = None
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def reverse_ll_rec1(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_ll_rec1(head.next)
    head.next.next = head
    head.next = None
    return new_head


def length_ll(head):
    count = 0
    while head is not None:
        head = head.next
        count += 1
    return count


def delete_ith_node_ll(i, head):
    if i < 0 or i > length_ll(head):
        return head
    curr = head
    tail = None
    count = 0
    if i is 0:
        head = head.next
        return head
    while curr is not None:
        if count == i:
            tail.next = curr.next
            return head
        tail = curr
        curr = curr.next
        count += 1


def delete_ith_node_rec_ll(head, i):
    if i is 0:
        return head.next
    temp = delete_ith_node_rec_ll(head.next, i-1)
    head.next = temp
    return head


def print_ll(head):
    while head is not None:
        print(head.data, "->", end="")
        head = head.next
    print("None")


def input_ll():
    li_val = [int(x) for x in input().split()]
    head = None
    tail = None
    for i in li_val:
        if i is -1:
            break
        new_node = Node(i)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head


Head = input_ll()
print_ll(Head)
# Head = reverse_ll(Head)
# print_ll(Head)
# Head = reverse_ll_rec1(Head)
# print_ll(Head)
# Head = delete_ith_node_ll(0, Head)
# print_ll(Head)
Head = delete_ith_node_rec_ll(Head, 1)
print_ll(Head)