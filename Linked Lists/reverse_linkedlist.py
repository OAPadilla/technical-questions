# Reverse a singly linked list.


class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def reverse_linkedlist(head):
    prev = None
    curr = head

    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    return prev
