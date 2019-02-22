

# 4.6 SUCCESSOR
def find_successor(node):
    # Leftmost node of node's right subtree
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node

    # If node doesn't have a right subtree, go up parents
    while node.parent and node.parent.right is node:
        node = node.parent

    # Once node isn't the parent's left child anymore then the root parent is next
    return node.parent
