# 2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
# node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

def intersection(head1, head2):
    len_h1 = 0
    len_h2 = 0
    curr1 = head1
    curr2 = head2
    # Find the sizes of the linked lists
    while curr1:
        len_h1 += 1
        curr1 = curr1.next
    while curr2:
        len_h2 += 1
        curr2 = curr2.next
    # Find the difference in sizes between the linked lists
    diff = abs(len_h1-len_h2)
    # Current node in longer list is then moved diff positions forward
    if len_h1 > len_h2:
        curr1 = head1
        for i in range(diff):
            curr1 = curr1.next
    else:
        curr2 = head2
        for i in range(diff):
            curr2 = curr2.next
    # Compare the nodes in both linked lists until intersection found
    while curr1 and curr2:
        if curr1 == curr2:
            return curr1
        else:
            curr1 = curr1.next
            curr2 = curr2.next
