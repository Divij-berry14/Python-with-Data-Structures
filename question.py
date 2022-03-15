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


def print_i_node_ll(head, i):
    curr = head
    count = 0
    while curr is not None:
        if count == i:
            return curr.data
        curr = curr.next
        count += 1


def insert_at_i_pos(head, i, data):
    if 0 > i > length_ll(head):
        return head
    curr = head
    count = 0
    prev = None
    while count < i:
        prev = curr
        curr = curr.next
        count += 1
    new_node = Node(data)
    if prev is None:
        head = new_node
    else:
        prev.next = new_node
    new_node.next = curr
    return head


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


def length_recursive(head):
    if head is None:
        return 0
    return 1 + length_recursive(head.next)


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


def delete_node_rec(head, i):
    if i < 0:
        return head

    if i is 0:
        return head.next

    small_head = delete_node_rec(head.next, i-1)
    head.next = small_head
    return head


def append_lst_n_to_first(head, n):
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


def eliminate_duplicate(head):
    curr = head
    while curr.next is not None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


def reverse_ll(head):
    curr = head
    prev = None
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def palindrome_ll(head):
    if head is None:
        return True
    s = []
    while head is not None:
        s.append(head.data)
        head = head.next
    right = len(s) - 1
    left = 0
    while left < right:
        if s[left] != s[right]:
            return False
        left = left + 1
        right = right - 1
    return True


def reverse_ll_rec(head):
    if head is None or head.next is None:
        return head
    small_head = reverse_ll_rec(head.next)
    head.next.next = head
    head.next = None
    return small_head


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
# print(length_ll(Head))
# print(print_i_node_ll(Head, 3))
# Head = insert_at_i_pos(Head, 2, 100)
# print_ll(Head)
# Head = delete_node(Head, 3)
# print_ll(Head)
print(length_recursive(Head))
# Head = insert_at_pos_rec(Head, 1, 70)
# print_ll(Head)
# Head = delete_node_rec(Head, 2)
# print_ll(Head)
# Head = append_lst_n_to_first(Head, 5)
# print_ll(Head)
# Head = eliminate_duplicate(Head)
# print_ll(Head)
# Head = reverse_ll(Head)
# print_ll(Head)
# print(palindrome_ll(Head))
Head = reverse_ll_rec(Head)
print_ll(Head)
