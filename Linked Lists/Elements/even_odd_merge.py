

# 7.10 IMPLEMENT EVEN-ODD MERGE
class ListNode:

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def even_odd_merge(head):
    if not head:
        return head

    even_h = even_ll = ListNode()
    odd_h = odd_ll = ListNode()

    tails = [even_ll, odd_ll]
    turn = 0

    while head:
        tails[turn].next = head
        head = head.next
        tails[turn] = tails[turn].next
        turn ^= 1   # alternates between even and odd

    even_ll.next = odd_h.next
    return even_h
