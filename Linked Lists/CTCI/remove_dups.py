# 2.1 Remove Dups! Write code to remove duplicates from an unsorted linked list.


class ListNode:

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def remove_dups(head):
    curr = head
    prev = ListNode()
    dups = {}

    while curr:
        if curr.data in dups:
            prev.next = curr.next
        else:
            dups[curr.data] = 1
            prev = curr
        curr = curr.next


def remove_dups_nobuffer(head):
    curr = head

    while curr:
        runner = curr
        while runner.next:
            if runner.next.data == curr.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr = curr.next
