# 2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.


class ListNode:

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def del_mid_node(node):
    if node is None or node.next is None:
        return False

    node.data = node.next.data
    node.next = node.next.next

    return True
