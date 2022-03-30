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

    small_head = insert_at_pos_rec(head.next, i - 1, data)
    head.next = small_head
    return head


def delete_node_rec(head, i):
    if i < 0:
        return head

    if i is 0:
        return head.next

    small_head = delete_node_rec(head.next, i - 1)
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


def reverse_ll_rec_2(head):
    if head is None or head.next is None:
        return head
    small_head = reverse_ll_rec_2(head.next)
    curr = small_head
    while curr.next is not None:
        curr = curr.next
    curr.next = head
    head.next = None
    return small_head


def reverse_ll_rec_3(head):
    if head is None or head.next is None:
        return head, head
    small_head, small_tail = reverse_ll_rec_3(head.next)
    small_tail.next = head
    head.next = None
    return small_head, head


def reverse_ll_rec_4(head):
    if head is None or head.next is None:
        return head
    small_head = reverse_ll_rec_4(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return small_head


def mid_point_ll(head):
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    print(str(slow.data))
    # length = length_ll(head) - 1
    # count = 0
    # while head is not None:
    #     if count == length//2:
    #         print(head.data)
    #         break
    #     head = head.next
    #     count += 1


def merge_sorted_ll(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data > head2.data:
        final_head = head2
        final_tail = head2
        head2 = head2.next
    else:
        final_head = head1
        final_tail = head1
        head1 = head1.next

    while head1 is not None and head2 is not None:
        if head1.data > head2.data:
            final_tail.next = head2
            final_tail = final_tail.next
            head2 = head2.next
        else:
            final_tail.next = head1
            final_tail = final_tail.next
            head1 = head1.next
    if head1 is not None:
        final_tail.next = head1
    if head2 is not None:
        final_tail.next = head2
    return final_head


def linear_search_recursive(head, n):
    if head is None:
        return -1
    if head.data == n:
        return 0
    temp = linear_search_recursive(head.next, n)
    if temp == -1:
        return -1
    return temp + 1


def odd_even_ll(head):
    if head is None:
        return head
    curr = head
    even_head = None
    even_tail = None
    odd_head = None
    odd_tail = None
    while curr is not None:
        if curr.data % 2 != 0:
            if odd_head is None:
                odd_head = curr
                odd_tail = curr
            else:
                odd_tail.next = curr
                odd_tail = curr
        else:
            if even_head is None:
                even_tail = curr
                even_head = curr
            else:
                even_tail.next = curr
                even_tail = curr
        curr = curr.next
    if odd_head is None:
        return even_head
    odd_tail.next = even_head
    return odd_head


def skip_m_delete_n(head, m, n):
    if m == 0:
        return
    if head is None or n <= 0 or m <= 0:
        return head
    curr = head
    while curr is not None:
        for i in range(m-1):
            if curr is None:
                break
            curr = curr.next
        prev = curr
        curr = curr.next
        for i in range(n):
            if curr is None:
                break
            curr = curr.next
        prev.next = curr
        # prev = curr
        # curr = curr.next
    return head


def swap_nodes_ll(head, i, j):
    curr = head
    count = 0
    x = 0
    y = 0
    if i == j:
        return head
    while curr is not None:
        if count == i:
            x = curr.data
        elif count == j:
            y = curr.data
        curr = curr.next
        count += 1
    if x == y:
        return head

    prev_x = None
    curr_x = head
    while curr_x is not None and curr_x.data != x:
        prev_x = curr_x
        curr_x = curr_x.next

    prev_y = None
    curr_y = head
    while curr_y is not None and curr_y.data != y:
        prev_y = curr_y
        curr_y = curr_y.next

    if curr_x is None or curr_y is None:
        return head

    if prev_x is not None:
        prev_x.next = curr_y
    else:
        head = curr_y

    if prev_y is not None:
        prev_y.next = curr_x
    else:
        head = curr_x

    temp = curr_x.next
    curr_x.next = curr_y.next
    curr_y.next = temp
    return head


def k_reverse(head, n):
    curr = head
    prev = None
    nex = None
    count = 0
    while curr is not None and count < n:
        pass


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
# print(length_recursive(Head))
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
# Head = reverse_ll_rec(Head)
# print_ll(Head)
# Head = reverse_ll_rec_2(Head)
# print_ll(Head)
# Head, Tail = reverse_ll_rec_3(Head)
# print_ll(Head)
# Head = reverse_ll_rec_4(Head)
# print_ll(Head)
# mid_point_ll(Head)
# Head1 = input_ll()
# Head2 = input_ll()
# print_ll(Head1)
# print_ll(Head2)
# Head = merge_sorted_ll(Head1, Head2)
# print_ll(Head)
# print(linear_search_recursive(Head, 20010))
# Head = odd_even_ll(Head)
# print_ll(Head)
# Head = skip_m_delete_n(Head, 3, 2)
# print_ll(Head)
Head = swap_nodes_ll(Head, 0, 4)
print_ll(Head)