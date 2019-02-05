# 2.8 Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.


class ListNode:

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def loop_detection(head):

    curr = head
    runner = head

    while runner is not None and runner.next is not None:
        curr = curr.next
        runner = runner.next.next
        if curr == runner:
            break

    if runner is None or runner.next is None:
        return None

    curr = head
    while runner != curr:
        curr = curr.next
        runner = runner.next

    return curr
