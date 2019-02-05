# 2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.


class ListNode:

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def kth_to_last(head, k):
    curr = head
    size = 0

    while curr:
        size += 1
        curr = curr.next

    curr = head
    for i in range(size-k+1):
        curr = curr.next
    return curr


def kth_to_last_iterative(head, k):
    curr1 = head
    curr2 = head

    for i in range(k):
        if curr1 is None:
            return None
        curr1 = curr1.next

    while curr1:
        curr1 = curr1.next
        curr2 = curr2.next

    return curr2



