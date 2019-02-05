

# 7.1 MERGE TWO SORTED LISTS
class ListNode:

    def __init__(self, data=0,next_node=None):
        self.data = data
        self.next = next_node


def merge_sorted_lists(head1, head2):
    merged_ll = ListNode()
    merged_head = merged_ll

    while head1 and head2:
        if head1.data < head2.data:
            merged_ll.next = head1
            head1 = head1.next
        else:
            merged_ll.next = head2
            head2 = head2.next
        merged_ll = merged_ll.next

    merged_ll.next = head1 or head2

    return merged_head
