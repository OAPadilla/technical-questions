# 2.6 Palindrome: Implement a function to check if a linked list is a palindrome


class ListNode:

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def is_palindrome(head):

    curr = head
    reversed = ListNode()
    rhead = reversed

    # create reversed LL
    while curr is not None:
        tmp = curr
        tmp.next = rhead.next   # Connects tmp to rhead ll
        rhead.next = tmp        # Update rhead.next to latest in the original ll thats been reversed
        curr = curr.next

    # compare both LLs
    reversed = reversed.next
    while head is not None:
        if head.data != reversed.data:
            return False
        head = head.next
        reversed = reversed.next

    return head is None and reversed is None
