

# 4.2 MINIMAL TREE
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def init_min_tree(a):
    return min_tree(a, 0, len(a)-1)


def min_tree(a, start, end):
    if start > end:
        return None
    # index of mid element in array
    mid = (start + end) // 2
    # initiate node with data = a[mid]
    root = TreeNode(a[mid])
    # recursive calls to the left and right children nodes
    root.left = min_tree(a, start, mid-1)
    root.right = min_tree(a, mid+1, end)
    return root

sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
init_min_tree(sorted_arr)
