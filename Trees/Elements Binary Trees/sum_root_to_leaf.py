

# 9.5 SUM THE ROOT-TO-LEAF PATHS IN A BINARY TREE
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sum_path(tree, partial_sum=0):
    if not tree:
        return 0

    partial_sum = partial_sum * 2 + tree.data
    # If node is a leaf
    if not tree.left and not tree.right:
        return partial_sum
    # If node is not a leaf, recursively move down tree and return sum of children
    return sum_path(tree.left, partial_sum) + sum_path(tree.right, partial_sum)
