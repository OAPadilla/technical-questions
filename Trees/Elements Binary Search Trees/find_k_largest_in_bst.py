

# 14.3 FIND THE K LARGEST ELEMENTS IN A BST
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_k_largest_in_bst(tree, k):
    k_largest_elements = []

    def helper(tree):
        # Reverse inorder
        if tree and len(k_largest_elements) < k:
            find_k_largest_in_bst(tree.right)
            if len(k_largest_elements) < k:
                k_largest_elements.append(tree.data)
                helper(tree.left)

    helper(tree)
    return k_largest_elements
