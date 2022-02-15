from sys import setrecursionlimit


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_node_rec(head, i):
    if i < 0:
        return head

    if i is 0:
        return head.next

    small_head = delete_node_rec(head.next, i-1)
    head.next = small_head
    return head


def ll(ar):
    if len(ar) is 0:
        return None
    head = Node(ar[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


def print_ll(head):
    while head is not None:
        print(head.data, "->", end="")
        head = head.next
    print("None")


setrecursionlimit(11000)
arr = list(int(i) for i in input().strip().split(' '))
li = ll(arr[:-1])
i = int(input())
li = delete_node_rec(li, i)
print_ll(li)
