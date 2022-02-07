from sys import setrecursionlimit


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length_recursive(head):
    if head is None:
        return 0

    return 1 + length_recursive(head.next)


def ll(ar):
    if len(ar) is 0:
        return None
    head = Node(ar[0])
    last = head
    for data in ar[1:]:
        last.next = Node(data)
        last = last.next
    return head


setrecursionlimit(11000)
arr = list(int(i) for i in input().strip().split(' '))
li = ll(arr[:-1])
length = length_recursive(li)
print(length)
