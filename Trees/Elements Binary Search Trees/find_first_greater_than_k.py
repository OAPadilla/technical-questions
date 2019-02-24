

# 14.2 FIND THE FIRST KEY GREATER THAN A GIVEN VALUE IN A BST
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_first_greater_than_k(root, k):
    curr_node = root
    first_so_far = None

    while curr_node:
        if curr_node.data > k:
            first_so_far = curr_node
            curr_node = curr_node.left
        else:
            curr_node = curr_node.right

    return first_so_far
