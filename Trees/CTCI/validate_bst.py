

# 4.5 VALIDATE BST: Implement a function to check if a binary tree is a binary search tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

prev = TreeNode(None)


def traverse_tree(root):

    global prev

    if root is None:
        return True

    if traverse_tree(root.left) is False:
        return False

    if prev is not None and root.data < prev.data:
        return False

    prev = root
    return traverse_tree(root.right)


def validate_bst(root):
    global prev
    prev = None
    return traverse_tree(root)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(validate_bst(root))
