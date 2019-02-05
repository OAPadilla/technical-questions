# 2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.


class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def partition(node, p):
    part1 = ListNode()
    part2 = ListNode()
    head = part1
    tail = part2

    while node:
        if node.data < p:
            part1.next = node
            part1 = part1.next
        else:
            part2.next = node
            part2 = part2.next
        node = node.next

    part1.next = tail.next

    return head.next
