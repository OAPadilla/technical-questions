import collections


# 9.1 TEST IF A BINARY TREE IS HEIGHT-BALANCED
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Solution 3 with Collections
def is_balanced_tree(root):
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height')
    )

    def check_balanced(root):
        # Base case
        if not root:
            return BalancedStatusWithHeight(True, -1)

        left_result = check_balanced(root.left)
        if not left_result.balanced:
            # Left subtree not balanced
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(root.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)


# Solution 2
def check_balanced(root):
    if root is None:
        return 0

    left_height = check_balanced(root.left)
    if left_height == -1:
        return -1

    right_height = check_balanced(root.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1


# Solution 1
def get_height(root):
    if root is None:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))


def is_balanced(root):
    if root is None:
        return True
    height_diff = abs(get_height(root.left) - get_height(root.right))
    if height_diff > 1:
        return False
    else:
        return is_balanced(root.left) and is_balanced(root.right)
