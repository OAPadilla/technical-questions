

# 4.2 MINIMAL TREE
sorted_arr = []

class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def min_tree(a):
    # index of mid element in array
    mid = len(a) // 2
    #
    root = TreeNode()
    root.data = a[mid]
    root.left = min_tree(a[:mid])
    root.right = min_tree(a[mid+1:])
    return root






min_tree(sorted_arr)
